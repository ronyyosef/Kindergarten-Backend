
import boto3
from boto3.dynamodb.conditions import Key

from const import TEACHERS_TABLE, PHONE_NUMBER, FIRST_NAME, LAST_NAME, PHOTO_LINK, KINDERGARTEN_ID, GROUP_NUMBER, \
    IS_ADMIN
from utils.logger import logger

teacher_table = boto3.resource('dynamodb').Table(TEACHERS_TABLE)


class TeacherHandler:

    @staticmethod
    def add_teacher(phone_number, first_name=None, last_name=None, photo_link=None, kindergarten_id=None,
                    group_number=None, is_admin=None):
        new_teacher = {
            PHONE_NUMBER: phone_number,
            FIRST_NAME: first_name,
            LAST_NAME: last_name,
            PHOTO_LINK: photo_link,
            KINDERGARTEN_ID: kindergarten_id,
            GROUP_NUMBER: group_number,
            IS_ADMIN: is_admin
        }
        try:
            logger.info(f'Adding teacher : {new_teacher}')
            response = teacher_table.put_item(Item=new_teacher)
            return response
        except Exception as e:
            logger.error(f'Cannot put {new_teacher} in {TEACHERS_TABLE}, {str(e)}')

    @staticmethod
    def get_teacher_data(phone_number):
        try:
            logger.info(f'Trying to get teacher: {phone_number}')
            response = teacher_table.query(KeyConditionExpression=Key(PHONE_NUMBER).eq(phone_number), Limit=1)
            teacher_data = response["Items"][0] if response['Count'] == 1 else None
            return teacher_data
        except Exception as e:
            logger.error(f'Error: {str(e)}')

    @staticmethod
    def update_teacher(phone_number, first_name=None, last_name=None, photo_link=None, kindergarten_id=None,
                       group_number=None, is_admin=None):
        try:
            response = teacher_table.update_item(
                Key={
                    PHONE_NUMBER: phone_number,
                },
                UpdateExpression=f'set {FIRST_NAME}=:1, {LAST_NAME}=:2,{PHOTO_LINK}=:3,{KINDERGARTEN_ID}=:4,{GROUP_NUMBER}=:5,{IS_ADMIN}=:6',
                ExpressionAttributeValues={
                    ':1': first_name,
                    ':2': last_name,
                    ':3': photo_link,
                    ':4': kindergarten_id,
                    ':5': group_number,
                    ':6': is_admin
                },
                ReturnValues='ALL_NEW'
            )
            return response['Attributes']
        except Exception as e:
            logger.error(f'Cannot update in {TEACHERS_TABLE}, {str(e)}')

    @staticmethod
    def delete_teacher(phone_number):
        response = teacher_table.delete_item(
            Key={
                PHONE_NUMBER: phone_number
            })
        return response

    @staticmethod
    def get_teacher_kindergarten_id(phone_number):
        teacher_data = TeacherHandler.get_teacher_data(phone_number)
        return teacher_data.get(KINDERGARTEN_ID)

