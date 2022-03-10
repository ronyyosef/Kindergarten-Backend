import boto3
from boto3.dynamodb.conditions import Key

from const import TEACHERS_TABLE, PHONE_NUMBER, FIRST_NAME, LAST_NAME, PHOTO_LINK, KINDERGARTEN_ID, GROUP_NUMBER, \
    IS_ADMIN, TEACHER_ID
from shared.S3PhotosHandler import S3PhotosHandler
from utils.logger import logger

teacher_table = boto3.resource('dynamodb').Table(TEACHERS_TABLE)


class TeacherHandler:

    @staticmethod
    def add_teacher(teacher_id: str, phone_number: str, first_name: str = None, last_name: str = None, kindergarten_id: str = None,
                    group_number: str = None, is_admin: str = None) -> None:
        new_teacher = {
            TEACHER_ID: teacher_id,
            PHONE_NUMBER: phone_number,
            FIRST_NAME: first_name,
            LAST_NAME: last_name,
            KINDERGARTEN_ID: kindergarten_id,
            GROUP_NUMBER: group_number,
            IS_ADMIN: is_admin
        }
        try:
            logger.info(f'Adding teacher : {new_teacher}')
            teacher_table.put_item(Item=new_teacher)
        except Exception as e:
            logger.error(f'Cannot put {new_teacher} in {TEACHERS_TABLE}, {str(e)}')

    @staticmethod
    def get_teacher_data(teacher_id: str) -> dict:
        try:
            logger.info(f'Trying to get teacher: {teacher_id}')
            response = teacher_table.query(KeyConditionExpression=Key(TEACHER_ID).eq(teacher_id), Limit=1)
            teacher_data = response["Items"][0] if response['Count'] == 1 else None
            if teacher_data:
                photo_url = S3PhotosHandler.get_photo_url(teacher_data[KINDERGARTEN_ID], teacher_id)
                teacher_data[PHOTO_LINK] = photo_url
            return teacher_data
        except Exception as e:
            logger.error(f'Error: {str(e)}')

    @staticmethod
    def update_teacher(teacher_id: str, first_name: str = None, last_name: str = None, kindergarten_id: str = None,
                       group_number: str = None, is_admin: str = None) -> None:
        try:
            response = teacher_table.update_item(
                Key={
                    TEACHER_ID: teacher_id,
                },
                UpdateExpression=f'set {FIRST_NAME}=:1, {LAST_NAME}=:2,{KINDERGARTEN_ID}=:3,{GROUP_NUMBER}=:4,{IS_ADMIN}=:5',
                ExpressionAttributeValues={
                    ':1': first_name,
                    ':2': last_name,
                    ':3': kindergarten_id,
                    ':4': group_number,
                    ':5': is_admin
                },
                ReturnValues='ALL_NEW'
            )
            return response['Attributes']
        except Exception as e:
            logger.error(f'Cannot update in {TEACHERS_TABLE}, {str(e)}')

    @staticmethod
    def delete_teacher(teacher_id: str) -> None:
        response = teacher_table.delete_item(
            Key={
                TEACHER_ID: teacher_id
            })

    @staticmethod
    def get_teacher_kindergarten_id(teacher_id: str) -> str:
        teacher_data = TeacherHandler.get_teacher_data(teacher_id)
        return teacher_data.get(KINDERGARTEN_ID)
