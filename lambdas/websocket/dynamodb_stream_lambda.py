import boto3
from boto3.dynamodb.table import BatchWriter, logger
from botocore.exceptions import ClientError

web_socket_client = boto3.client('apigatewaymanagementapi',
                                 endpoint_url='https://1f8qirmdzh.execute-api.us-east-1.amazonaws.com/dev')


def send_message(event, context):
    logger.info(event)
    logger.info(context)
    table = boto3.resource('dynamodb').Table('Websocket')
    response = table.scan()
    for item in response["Items"]:
        connection = item['connection_id']
        try:
            web_socket_client.post_to_connection(
                Data='some data',
                ConnectionId=connection
            )
        except ClientError as ex:
            table.delete_item(Key={"connection_id": connection})