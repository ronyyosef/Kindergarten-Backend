from datetime import date

import boto3
from boto3.dynamodb.conditions import Key

from const import ATTENDANCE_TABLE, ATTENDANCE_PK, ATTENDANCE_SK, KINDERGARTEN_ID, HAS_ARRIVED
from utils.logger import logger

attendance_table = boto3.resource('dynamodb').Table(ATTENDANCE_TABLE)


class AttendanceHandler:

    @staticmethod
    def add_attendance(child_id: str, kindergarten_id: str, has_arrived: str):
        new_attendance = {
            ATTENDANCE_PK: child_id,
            ATTENDANCE_SK: str(date.today()),
            KINDERGARTEN_ID: kindergarten_id,
            HAS_ARRIVED: has_arrived
        }
        try:
            return attendance_table.put_item(Item=new_attendance)
        except Exception as e:
            logger.error(f'Cannot put {new_attendance} in {ATTENDANCE_TABLE}, {str(e)}')

    @staticmethod
    def get_attendance(child_id, date_query):
        response = attendance_table.query(
            KeyConditionExpression=Key(ATTENDANCE_PK).eq(child_id) & Key(ATTENDANCE_SK).eq(date_query))
        return response['Items'][0]

    @staticmethod
    def delete_attendance(child_id, date_query):
        response = attendance_table.delete_item(

            Key={
                ATTENDANCE_PK: child_id,
                ATTENDANCE_SK: date_query
            })
        return response

    @staticmethod
    def update_attendance(child_id, date_query, kindergarten_id: str, has_arrived: str):
        try:
            response = attendance_table.update_item(
                Key={
                    ATTENDANCE_PK: child_id,
                    ATTENDANCE_SK: date_query
                },
                UpdateExpression=f'set {KINDERGARTEN_ID}=:1, {HAS_ARRIVED}=:2',
                ExpressionAttributeValues={
                    ':1': kindergarten_id,
                    ':2': has_arrived
                },
                ReturnValues='ALL_NEW'
            )
            return response['Attributes']
        except Exception as e:
            logger.error(f'Cannot update in {ATTENDANCE_TABLE}, {str(e)}')


