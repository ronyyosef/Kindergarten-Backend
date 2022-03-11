import logging

import boto3
from boto3.dynamodb.table import TableResource, BatchWriter

from shared.hanlders.lambda_decorator import lambda_decorator

event = {'headers': {'Host': '6t7ekp92lc.execute-api.us-east-1.amazonaws.com',
                     'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
                     'Sec-WebSocket-Key': 'k9mtrXaBvJrgXiHYShuQIw==', 'Sec-WebSocket-Version': '13',
                     'X-Amzn-Trace-Id': 'Root=1-622a2b67-06b6e5ea4ca158dd0b19fcdf', 'X-Forwarded-For': '5.102.253.21',
                     'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'},
         'multiValueHeaders': {'Host': ['6t7ekp92lc.execute-api.us-east-1.amazonaws.com'],
                               'Sec-WebSocket-Extensions': ['permessage-deflate; client_max_window_bits'],
                               'Sec-WebSocket-Key': ['k9mtrXaBvJrgXiHYShuQIw=='], 'Sec-WebSocket-Version': ['13'],
                               'X-Amzn-Trace-Id': ['Root=1-622a2b67-06b6e5ea4ca158dd0b19fcdf'],
                               'X-Forwarded-For': ['5.102.253.21'], 'X-Forwarded-Port': ['443'],
                               'X-Forwarded-Proto': ['https']},
         'requestContext': {'routeKey': '$connect', 'eventType': 'CONNECT', 'extendedRequestId': 'Oxu4RHWfoAMF-Eg=',
                            'requestTime': '10/Mar/2022:16:46:31 +0000', 'messageDirection': 'IN', 'stage': 'dev',
                            'connectedAt': 1646930791964, 'requestTimeEpoch': 1646930791966,
                            'identity': {'sourceIp': '5.102.253.21'}, 'requestId': 'Oxu4RHWfoAMF-Eg=',
                            'domainName': '6t7ekp92lc.execute-api.us-east-1.amazonaws.com',
                            'connectionId': 'Oxu4RfhJoAMCKPw=',
                            'apiId': '6t7ekp92lc'}, 'isBase64Encoded': False}

from utils.logger import logger


# @lambda_decorator
def connect(event, context):
    logger.info(event)
    connectionID = event["requestContext"]["connectionId"]
    table: BatchWriter = boto3.resource('dynamodb').Table('Websocket')
    table.put_item(Item={"connection_id": connectionID})
    return {"statusCode": 200, "body": 'some body'}


connect(event, {})
