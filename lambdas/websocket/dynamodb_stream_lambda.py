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


event = {'Records': [{'eventID': 'b22a9c3e88bb98bb34d7e9ee63d45d7b', 'eventName': 'MODIFY', 'eventVersion': '1.1',
                      'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-1',
                      'dynamodb': {'ApproximateCreationDateTime': 1647000014.0, 'Keys': {'date': {'S': '2022-03-11'},
                                                                                         'child_id': {
                                                                                             'S': 'd4840ab8-cce9-4d9c-9d97-535d07af938b'}},
                                   'NewImage': {'date': {'S': '2022-03-11'}, 'is_present': {'S': 'yes'},
                                                'child_id': {'S': 'd4840ab8-cce9-4d9c-9d97-535d07af938b'},
                                                'kindergarten_id': {'S': '932fccce'}, 'time_in': {'S': '13:57:45'},
                                                'ttl': {'N': '1650017821'}, 'time_out': {'NULL': True}},
                                   'SequenceNumber': '2117300000000025896682126', 'SizeBytes': 185,
                                   'StreamViewType': 'NEW_IMAGE'},
                      'eventSourceARN': 'arn:aws:dynamodb:us-east-1:344089725894:table/AttendanceData/stream/2022-03-11T07:38:18.497'},
                     {'eventID': 'b4797cb04277c97a8a98b497091f5148', 'eventName': 'MODIFY', 'eventVersion': '1.1',
                      'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-1',
                      'dynamodb': {'ApproximateCreationDateTime': 1647000042.0, 'Keys': {'date': {'S': '2022-03-11'},
                                                                                         'child_id': {
                                                                                             'S': 'd4840ab8-cce9-4d9c-9d97-535d07af938b'}},
                                   'NewImage': {'date': {'S': '2022-03-11'}, 'is_present': {'S': 'no'},
                                                'child_id': {'S': 'd4840ab8-cce9-4d9c-9d97-535d07af938b'},
                                                'kindergarten_id': {'S': '932fccce'}, 'time_in': {'S': '13:57:45'},
                                                'ttl': {'N': '1650017821'}, 'time_out': {'S': '14:00:57'}},
                                   'SequenceNumber': '2117400000000025896697976', 'SizeBytes': 191,
                                   'StreamViewType': 'NEW_IMAGE'},
                      'eventSourceARN': 'arn:aws:dynamodb:us-east-1:344089725894:table/AttendanceData/stream/2022-03-11T07:38:18.497'},
                     {'eventID': '37fde08af91080dc9d01322df47447c0', 'eventName': 'MODIFY', 'eventVersion': '1.1',
                      'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-1',
                      'dynamodb': {'ApproximateCreationDateTime': 1647000631.0, 'Keys': {'date': {'S': '2022-03-11'},
                                                                                         'child_id': {
                                                                                             'S': '56a429f7-a345-473d-8515-b9cdcc180f86'}},
                                   'NewImage': {'date': {'S': '2022-03-11'},
                                                'child_id': {'S': '56a429f7-a345-473d-8515-b9cdcc180f86'},
                                                'kindergarten_id': {'S': 'db7471eb'}, 'time_in': {'S': '11:54:23'},
                                                'ttl': {'N': '1650023663'}, 'time_out': {'S': '12:10:31'}},
                                   'SequenceNumber': '2117500000000025897037091', 'SizeBytes': 179,
                                   'StreamViewType': 'NEW_IMAGE'},
                      'eventSourceARN': 'arn:aws:dynamodb:us-east-1:344089725894:table/AttendanceData/stream/2022-03-11T07:38:18.497'},
                     {'eventID': '7d5a005fa77e0f1621adefe2cda6d0cb', 'eventName': 'MODIFY', 'eventVersion': '1.1',
                      'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-1',
                      'dynamodb': {'ApproximateCreationDateTime': 1647000636.0, 'Keys': {'date': {'S': '2022-03-11'},
                                                                                         'child_id': {
                                                                                             'S': '56a429f7-a345-473d-8515-b9cdcc180f86'}},
                                   'NewImage': {'date': {'S': '2022-03-11'},
                                                'child_id': {'S': '56a429f7-a345-473d-8515-b9cdcc180f86'},
                                                'kindergarten_id': {'S': 'db7471eb'}, 'time_in': {'S': '11:54:23'},
                                                'ttl': {'N': '1650023663'}, 'time_out': {'S': '12:10:36'}},
                                   'SequenceNumber': '2117600000000025897040831', 'SizeBytes': 179,
                                   'StreamViewType': 'NEW_IMAGE'},
                      'eventSourceARN': 'arn:aws:dynamodb:us-east-1:344089725894:table/AttendanceData/stream/2022-03-11T07:38:18.497'},
                     {'eventID': '82c71e55400bcdeade8fdf3952011f8d', 'eventName': 'REMOVE', 'eventVersion': '1.1',
                      'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-1',
                      'dynamodb': {'ApproximateCreationDateTime': 1647000737.0, 'Keys': {'date': {'S': '2022-03-11'},
                                                                                         'child_id': {
                                                                                             'S': '1a64f328-b872-4049-b3d4-5d7a4c7fe3d6'}},
                                   'SequenceNumber': '2117700000000025897106298', 'SizeBytes': 58,
                                   'StreamViewType': 'NEW_IMAGE'},
                      'eventSourceARN': 'arn:aws:dynamodb:us-east-1:344089725894:table/AttendanceData/stream/2022-03-11T07:38:18.497'},
                     {'eventID': 'c093002ca74f0f0c5cc949fef57d5322', 'eventName': 'REMOVE', 'eventVersion': '1.1',
                      'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-1',
                      'dynamodb': {'ApproximateCreationDateTime': 1647000737.0, 'Keys': {'date': {'S': '2022-03-11'},
                                                                                         'child_id': {
                                                                                             'S': '754265e7-3e34-469b-b149-bb2ed2cb619d'}},
                                   'SequenceNumber': '2117800000000025897106402', 'SizeBytes': 58,
                                   'StreamViewType': 'NEW_IMAGE'},
                      'eventSourceARN': 'arn:aws:dynamodb:us-east-1:344089725894:table/AttendanceData/stream/2022-03-11T07:38:18.497'},
                     {'eventID': '6512d118126c1a75804777c5465d07de', 'eventName': 'REMOVE', 'eventVersion': '1.1',
                      'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-1',
                      'dynamodb': {'ApproximateCreationDateTime': 1647000737.0, 'Keys': {'date': {'S': '2022-03-11'},
                                                                                         'child_id': {
                                                                                             'S': '56a429f7-a345-473d-8515-b9cdcc180f86'}},
                                   'SequenceNumber': '2117900000000025897106404', 'SizeBytes': 58,
                                   'StreamViewType': 'NEW_IMAGE'},
                      'eventSourceARN': 'arn:aws:dynamodb:us-east-1:344089725894:table/AttendanceData/stream/2022-03-11T07:38:18.497'}]}

send_message(event, {})
