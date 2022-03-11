from utils.logger import logger
import logging
import jwt
import boto3
from boto3.dynamodb.table import TableResource, BatchWriter

from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator

event = {'headers': {'Host': 'websocket.kindergartenil.com',
                     'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
                     'Sec-WebSocket-Key': 'l2tTfO8DzF/h01jLYvWZ/g==', 'Sec-WebSocket-Version': '13',
                     'X-Amzn-Trace-Id': 'Root=1-622b0ecc-1957dfa66863fb2260a2fd13', 'X-Forwarded-For': '5.102.253.21',
                     'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'},
         'multiValueHeaders': {'Host': ['websocket.kindergartenil.com'],
                               'Sec-WebSocket-Extensions': ['permessage-deflate; client_max_window_bits'],
                               'Sec-WebSocket-Key': ['l2tTfO8DzF/h01jLYvWZ/g=='], 'Sec-WebSocket-Version': ['13'],
                               'X-Amzn-Trace-Id': ['Root=1-622b0ecc-1957dfa66863fb2260a2fd13'],
                               'X-Forwarded-For': ['5.102.253.21'], 'X-Forwarded-Port': ['443'],
                               'X-Forwarded-Proto': ['https']}, 'queryStringParameters': {
    'token': 'eyJraWQiOiJjTzdiaG40ckRRVjJWamszdUwyR2dmSUg3S2FpR1YzdmJta3cwNEhlMmZZPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiQXNlS0syejExaGFIanA2Y0U2TWNSQSIsInN1YiI6ImFlOTg1OWJiLTVjZWMtNGFkZS1iMzJlLWNmOGJlZmYyYTllZCIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX1Bva2plc2hYMyIsInBob25lX251bWJlcl92ZXJpZmllZCI6ZmFsc2UsImNvZ25pdG86dXNlcm5hbWUiOiJhZTk4NTliYi01Y2VjLTRhZGUtYjMyZS1jZjhiZWZmMmE5ZWQiLCJhdWQiOiIzNmQ4b3B1N2oyZTlpbGxnZTZ2bGZqZHU5aCIsImV2ZW50X2lkIjoiNTNiZjIxYTYtNmI5NC00NmU1LWJhY2ItYzEzYmI1YTkxZTlkIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2NDY5ODQwMDksInBob25lX251bWJlciI6Iis5NzI1MzI4NDAzODgiLCJleHAiOjE2NDcwNzA0MDksImlhdCI6MTY0Njk4NDAwOSwianRpIjoiNjY3MTU1ZWEtODdmOS00MTY0LTg4MzMtODU0NTQzNzhmNWJkIn0.uHObwjfzjE94QlTOV8BvE7Tnd1tNcIKH_1BUCtBakY4uGoe51xdScHGHi7dF4V2LHQx1rnRwG7aU_tSxqb_omD1emKsOKSMOBU89E3Ai-GvdnXrAaW9lHsINWR7qtdjBjy1Uk78uGz4BxZwTIpVmmxtTUJ9C3Tv38dnqQU2rrznRy5BTKlNYj-Dny5DEcTfIQiQxj-VKAp8zyJSnzqG0XvLhxp7oWXZKUJUKo9OaZ7qq6hEGWn13vMukzObB_0-HV-Q2vfPNTrHwwQaE1CDHxaHXgbzECylzYU6mKHvc5f3pLp-uNMcUIidvIxz_gkU8vHPu4WrzZsdB5O0MKU0d0g'},
    'multiValueQueryStringParameters': {'token': [
        'eyJraWQiOiJjTzdiaG40ckRRVjJWamszdUwyR2dmSUg3S2FpR1YzdmJta3cwNEhlMmZZPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiQXNlS0syejExaGFIanA2Y0U2TWNSQSIsInN1YiI6ImFlOTg1OWJiLTVjZWMtNGFkZS1iMzJlLWNmOGJlZmYyYTllZCIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX1Bva2plc2hYMyIsInBob25lX251bWJlcl92ZXJpZmllZCI6ZmFsc2UsImNvZ25pdG86dXNlcm5hbWUiOiJhZTk4NTliYi01Y2VjLTRhZGUtYjMyZS1jZjhiZWZmMmE5ZWQiLCJhdWQiOiIzNmQ4b3B1N2oyZTlpbGxnZTZ2bGZqZHU5aCIsImV2ZW50X2lkIjoiNTNiZjIxYTYtNmI5NC00NmU1LWJhY2ItYzEzYmI1YTkxZTlkIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2NDY5ODQwMDksInBob25lX251bWJlciI6Iis5NzI1MzI4NDAzODgiLCJleHAiOjE2NDcwNzA0MDksImlhdCI6MTY0Njk4NDAwOSwianRpIjoiNjY3MTU1ZWEtODdmOS00MTY0LTg4MzMtODU0NTQzNzhmNWJkIn0.uHObwjfzjE94QlTOV8BvE7Tnd1tNcIKH_1BUCtBakY4uGoe51xdScHGHi7dF4V2LHQx1rnRwG7aU_tSxqb_omD1emKsOKSMOBU89E3Ai-GvdnXrAaW9lHsINWR7qtdjBjy1Uk78uGz4BxZwTIpVmmxtTUJ9C3Tv38dnqQU2rrznRy5BTKlNYj-Dny5DEcTfIQiQxj-VKAp8zyJSnzqG0XvLhxp7oWXZKUJUKo9OaZ7qq6hEGWn13vMukzObB_0-HV-Q2vfPNTrHwwQaE1CDHxaHXgbzECylzYU6mKHvc5f3pLp-uNMcUIidvIxz_gkU8vHPu4WrzZsdB5O0MKU0d0g']},
    'requestContext': {'routeKey': '$connect', 'eventType': 'CONNECT', 'extendedRequestId': 'Oz8_-FqUoAMF_vQ=',
                       'requestTime': '11/Mar/2022:08:56:44 +0000', 'messageDirection': 'IN', 'stage': 'dev',
                       'connectedAt': 1646989004400, 'requestTimeEpoch': 1646989004401,
                       'identity': {'sourceIp': '5.102.253.21'}, 'requestId': 'Oz8_-FqUoAMF_vQ=',
                       'domainName': 'websocket.kindergartenil.com', 'connectionId': 'Oz8_-123-qoAMC123LMg=',
                       'apiId': '0ocw2ogu91'}, 'isBase64Encoded': False}


def connect(event, context):
    logger.info(event)
    # add verify
    user_name = jwt.decode(event['queryStringParameters']['token'], options={
                           "verify_signature": False})['cognito:username']
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(user_name)
    connectionID = event["requestContext"]["connectionId"]
    table = boto3.resource('dynamodb').Table('WebsocketConnectionManager')
    table.put_item(Item={"connection_id": connectionID,
                   'kindergarten_id': kindergarten_id})
    return {"statusCode": 200, "body": 'connect successfully'}


connect(event, {})
