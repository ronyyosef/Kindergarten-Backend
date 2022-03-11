import json

import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from shared.const import KINDERGARTEN_ID
from utils.logger import logger

web_socket_client = boto3.client('apigatewaymanagementapi',
                                 endpoint_url='https://websocket.kindergartenil.com')


def send_message(event, context):
    try:
        logger.info(event)
        table = boto3.resource('dynamodb').Table('WebsocketConnectionManager')
        for record in event['Records']:
            if record['eventName'] == 'REMOVE': break
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
                except ClientError as ex:
                    table.delete_item(Key={"connection_id": connection})
    except:
        pass


event = {'Records': [{'eventID': '5857c20557b424606ec2c6bcdd361b71', 'eventName': 'INSERT', 'eventVersion': '1.1',
                      'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-1',
                      'dynamodb': {'ApproximateCreationDateTime': 1647018833.0, 'Keys': {'date': {'S': '2022-03-11'},
                                                                                         'child_id': {
                                                                                             'S': 'cf3ee872-9c0e-44cd-8081-48dd8455c97a'}},
                                   'NewImage': {'date': {'S': '2022-03-11'}, 'is_present': {'S': 'no'},
                                                'child_id': {'S': 'cf3ee872-9c0e-44cd-8081-48dd8455c97a'},
                                                'kindergarten_id': {'S': '88ef543b'}, 'time_in': {'NULL': True},
                                                'ttl': {'N': '1650042833'}, 'time_out': {'NULL': True}},
                                   'SequenceNumber': '2992700000000000406987624', 'SizeBytes': 177,
                                   'StreamViewType': 'NEW_IMAGE'},
                      'eventSourceARN': 'arn:aws:dynamodb:us-east-1:344089725894:table/AttendanceData/stream/2022-03-11T07:38:18.497'},
                     {'eventID': 'c7d001fc7ffd633b8141ee1ad6ce7a6b', 'eventName': 'MODIFY', 'eventVersion': '1.1',
                      'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-1',
                      'dynamodb': {'ApproximateCreationDateTime': 1647018833.0, 'Keys': {'date': {'S': '2022-03-11'},
                                                                                         'child_id': {
                                                                                             'S': 'cf3ee872-9c0e-44cd-8081-48dd8455c97a'}},
                                   'NewImage': {'date': {'S': '2022-03-11'}, 'is_present': {'S': 'no'},
                                                'child_id': {'S': 'cf3ee872-9c0e-44cd-8081-48dd8455c97a'},
                                                'kindergarten_id': {'S': '88ef543b'}, 'time_in': {'NULL': True},
                                                'ttl': {'N': '1650042833'}, 'time_out': {'S': '17:13:53'}},
                                   'SequenceNumber': '2992800000000000406987658', 'SizeBytes': 184,
                                   'StreamViewType': 'NEW_IMAGE'},
                      'eventSourceARN': 'arn:aws:dynamodb:us-east-1:344089725894:table/AttendanceData/stream/2022-03-11T07:38:18.497'}]}

send_message(event, {})
