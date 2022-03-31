import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

from shared.const import TEACHERS_TABLE, PHONE_NUMBER, FIRST_NAME, LAST_NAME, \
    PHOTO_LINK, KINDERGARTEN_ID, GROUP_NAME, TEACHER_ID
from shared.error_handling.error_codes import INPUT_ERROR
from shared.error_handling.exception import MyException
from shared.hanlders.GroupsHandler import GroupsHandler
from shared.hanlders.S3PhotosHandler import S3PhotosHandler
from utils.logger import logger

teacher_table = boto3.resource('dynamodb').Table(TEACHERS_TABLE)


class TeacherHandler:

    @staticmethod
    def add_teacher(
            teacher_id: str,
            phone_number: str,
            first_name: str = None,
            last_name: str = None,
            kindergarten_id: str = None,
            group_name: str = None,
    ) -> None:
        new_teacher = {
            TEACHER_ID: teacher_id,
            PHONE_NUMBER: phone_number,
            FIRST_NAME: first_name,
            LAST_NAME: last_name,
            KINDERGARTEN_ID: kindergarten_id,
            GROUP_NAME: group_name,
        }
        logger.info(f'Adding teacher : {new_teacher}')
        teacher_table.put_item(Item=new_teacher)

    @staticmethod
    def get_teacher_data(teacher_id: str) -> dict:
        logger.info(f'Trying to get teacher: {teacher_id}')
        response = teacher_table.query(
            KeyConditionExpression=Key(TEACHER_ID).eq(teacher_id), Limit=1)
        teacher_data = response["Items"][0] if response['Count'] == 1 else None
        if teacher_data is None:
            raise MyException('Teacher not exist', INPUT_ERROR)
        if teacher_data:
            photo_url = S3PhotosHandler.get_photo_url(
                teacher_data[KINDERGARTEN_ID], teacher_id)
            teacher_data[PHOTO_LINK] = photo_url
        return teacher_data

    @staticmethod
    def update_teacher(
            teacher_id: str,
            first_name: str = None,
            last_name: str = None,
            kindergarten_id: str = None,
            group_name: str = None,
    ) -> None:
        response = teacher_table.update_item(
            Key={
                TEACHER_ID: teacher_id,
            },
            UpdateExpression=f'set {FIRST_NAME}=:1, {LAST_NAME}=:2,{KINDERGARTEN_ID}=:3,{GROUP_NAME}=:4',
            ExpressionAttributeValues={
                ':1': first_name,
                ':2': last_name,
                ':3': kindergarten_id,
                ':4': group_name},
            ReturnValues='ALL_NEW')
        return response['Attributes']

    @staticmethod
    def delete_teacher(teacher_id: str) -> None:
        teacher_table.delete_item(
            Key={
                TEACHER_ID: teacher_id
            })

    @staticmethod
    def get_teacher_kindergarten_id(teacher_id: str) -> str:
        teacher_data = TeacherHandler.get_teacher_data(teacher_id)
        return teacher_data.get(KINDERGARTEN_ID)

    @staticmethod
    def update_teacher_name(
            teacher_id: str,
            first_name: str,
            last_name: str) -> dict:
        response = teacher_table.get_item(Key={
            TEACHER_ID: teacher_id
        })
        item = response['Item']

        if first_name is not None:
            item[FIRST_NAME] = first_name
        if last_name is not None:
            item[LAST_NAME] = last_name
        teacher_table.put_item(Item=item)
        return item

    @staticmethod
    def update_teacher_group_name(teacher_data: dict, group_name: str):
        if GroupsHandler.group_exist(
                kindergarten_id=teacher_data[KINDERGARTEN_ID],
                group_name=group_name) is False:
            raise MyException("group_name not exist", INPUT_ERROR)

        teacher_data[GROUP_NAME] = group_name
        teacher_table.put_item(Item=teacher_data)

        return teacher_data

    @staticmethod
    def get_all_teacher_in_group(teacher_data, group_name):
        response = teacher_table.scan(
            FilterExpression=Key(KINDERGARTEN_ID).eq(
                teacher_data[KINDERGARTEN_ID]) & Attr(GROUP_NAME).eq(
                group_name))
        return response['Items']
