import json
import logging

import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from shared.const import KINDERGARTEN_ID
from utils.logger import logger

web_socket_client = boto3.client(
    'apigatewaymanagementapi',
    endpoint_url='https://websocket.kindergartenil.com')


def send_message(event, context):
    try:
        logger.info(event)
        table = boto3.resource('dynamodb').Table('WebsocketConnectionManager')
        for record in event['Records']:
            if record['eventName'] == 'REMOVE':
                break
            data = record['dynamodb']['NewImage']
            child_id = data['child_id']['S']
            kindergarten_id = data['kindergarten_id']['S']
            is_present = data['is_present']['S']
            message = {'child_id': child_id, "is_present": is_present}
            response = table.query(
                IndexName='kindergarten_id_index',
                KeyConditionExpression=Key(KINDERGARTEN_ID).eq(kindergarten_id)
            )
            for item in response["Items"]:
                connection = item['connection_id']
                try:
                    web_socket_client.post_to_connection(
                        Data=json.dumps(message),
                        ConnectionId=connection
                    )
                except ClientError:
                    table.delete_item(Key={"connection_id": connection})
    except Exception as ex:
        logging.info(str(ex))