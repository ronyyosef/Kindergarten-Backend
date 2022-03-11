import boto3
import jwt

from shared.hanlders.TeacherHandler import TeacherHandler
from utils.logger import logger


def connect(event, context):
    logger.info(event)
    # add verify
    user_name = jwt.decode(event['queryStringParameters']['token'], options={
        "verify_signature": False})['cognito:username']
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(user_name)
    connection_id = event["requestContext"]["connectionId"]
    table = boto3.resource('dynamodb').Table('WebsocketConnectionManager')
    table.put_item(Item={"connection_id": connection_id,
                         'kindergarten_id': kindergarten_id})
    return {"statusCode": 200, "body": 'connect successfully'}
