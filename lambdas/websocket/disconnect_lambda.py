import logging

import boto3
from boto3.dynamodb.table import BatchWriter

from shared.hanlders.lambda_decorator import lambda_decorator

# @lambda_decorator
from utils.logger import logger

event = {'headers': {'Host': '6t7ekp92lc.execute-api.us-east-1.amazonaws.com', 'x-api-key': '', 'X-Forwarded-For': '',
                     'x-restapi': ''},
         'multiValueHeaders': {'Host': ['6t7ekp92lc.execute-api.us-east-1.amazonaws.com'], 'x-api-key': [''],
                               'X-Forwarded-For': [''], 'x-restapi': ['']},
         'requestContext': {'routeKey': '$disconnect', 'disconnectStatusCode': 1005, 'eventType': 'DISCONNECT',
                            'extendedRequestId': 'OxxXgGPmoAMFiQQ=', 'requestTime': '10/Mar/2022:17:03:31 +0000',
                            'messageDirection': 'IN', 'disconnectReason': 'Client-side close frame status not set',
                            'stage': 'dev', 'connectedAt': 1646931807909, 'requestTimeEpoch': 1646931811062,
                            'identity': {'sourceIp': '5.102.253.21'}, 'requestId': 'OxxXgGPmoAMFiQQ=',
                            'domainName': '6t7ekp92lc.execute-api.us-east-1.amazonaws.com',
                            'connectionId': 'OxxXBfG1oAMActQ=', 'apiId': '6t7ekp92lc'}, 'isBase64Encoded': False}


def disconnect(event, context):
    logger.info(event)
    connectionID = event["requestContext"]["connectionId"]
    table: BatchWriter = boto3.resource('dynamodb').Table('WebsocketConnectionManager01')
    table.delete_item(Key={"connection_id": 'OxxXgGPmoAMFiQQ='})
    return {"statusCode": 200, "body": 'some body'}


disconnect(event, {})
