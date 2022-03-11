import boto3
from botocore.exceptions import ClientError

from utils.logger import logger

web_socket_client = boto3.client('apigatewaymanagementapi',
                                 endpoint_url='https://websocket.kindergartenil.com')
# # MODIFY
# event = {'Records': [{'eventID': '851163a450805a957c316866fca2a3da', 'eventName': 'MODIFY', 'eventVersion': '1.1',
#                       'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-1',
#                       'dynamodb': {'ApproximateCreationDateTime': 1646949797.0, 'Keys': {'date': {'S': '2022-03-10'},
#                                                                                          'child_id': {
#                                                                                              'S': '90e7dca0-3f8c-4713-aee6-a715455b857f'}},
#                                    'NewImage': {'date': {'S': '2022-03-10'},
#                                                 'child_id': {'S': '90e7dca0-3f8c-4713-aee6-a715455b857f'},
#                                                 'kindergarten_id': {'S': 'a949ee75'}, 'time_in': {'S': '18:59:03'},
#                                                 'ttl': {'N': '1649955555'}, 'time_out': {'S': '19:08:59'}},
#                                    'SequenceNumber': '9192100000000025472410832', 'SizeBytes': 179,
#                                    'StreamViewType': 'NEW_IMAGE'},
#                       'eventSourceARN': 'arn:aws:dynamodb:us-east-1:344089725894:table/AttendanceData/stream/2022-03-10T20:51:31.023'}]}
# # INSERT
# event2 = {'Records': [{'eventID': '67220458628aed3fe5748d707795fb37', 'eventName': 'INSERT', 'eventVersion': '1.1',
#                        'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-1',
#                        'dynamodb': {'ApproximateCreationDateTime': 1646950565.0,
#                                     'Keys': {'date': {'S': '123123213'}, 'child_id': {'S': '123123'}},
#                                     'NewImage': {'date': {'S': '123123213'}, 'child_id': {'S': '123123'}},
#                                     'SequenceNumber': '9192300000000025472886698', 'SizeBytes': 54,
#                                     'StreamViewType': 'NEW_IMAGE'},
#                        'eventSourceARN': 'arn:aws:dynamodb:us-east-1:344089725894:table/AttendanceData/stream/2022-03-10T20:51:31.023'}]}
#

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
