from typing import List

import boto3
from boto3.dynamodb.conditions import Key

from const import CHILD_TABLE, KINDERGARTEN_ID, FIRST_NAME, ID, LAST_NAME, \
    GROUP_NUMBER, PARENT1_PHONE_NUMBER, PARENT2_PHONE_NUMBER, PHOTO_LINK
from shared.S3PhotosHandler import S3PhotosHandler
from utils.logger import logger

child_table = boto3.resource('dynamodb').Table(CHILD_TABLE)


class ChildrenHandler:
    @staticmethod
    def add_child(id: str, kindergarten_id: str, first_name: str, last_name: str, group_number: str,
                  parent1_phone_number: str,
                  parent2_phone_number: str = None):

        new_child = {
            ID: id,
            KINDERGARTEN_ID: kindergarten_id,
            FIRST_NAME: first_name,
            LAST_NAME: last_name,
            GROUP_NUMBER: group_number,
            PARENT1_PHONE_NUMBER: parent1_phone_number,
            PARENT2_PHONE_NUMBER: parent2_phone_number,
        }

        try:
            return child_table.put_item(Item=new_child)
        except Exception as e:
            logger.error(f'Cannot put {new_child} in {CHILD_TABLE}, {str(e)}')

    @staticmethod
    def get_child(id):
        response = child_table.query(
            KeyConditionExpression=Key(ID).eq(id))
        result = response['Items'][0]
        photo_url = S3PhotosHandler.get_photo_url(result[KINDERGARTEN_ID], id)
        result[PHOTO_LINK] = photo_url
        return result

    @staticmethod
    def check_if_key_exists(key_to_search):
        response = child_table.query(
            KeyConditionExpression=Key(ID).eq(key_to_search))
        return len(response["Items"]) > 0

    @staticmethod
    def get_children_for_kindergarten(kindergarten_id: str) -> List[dict]:
        response = child_table.scan(
            FilterExpression=Key(KINDERGARTEN_ID).eq(kindergarten_id))
        for item in response['Items']:
            photo_url = S3PhotosHandler.get_photo_url(kindergarten_id, item[ID])
            item[PHOTO_LINK] = photo_url
        return response['Items']

    @staticmethod
    def child_in_kindergarten(child_id: str, kindergarten_id: str) -> bool:
        response = child_table.query(
            KeyConditionExpression=f'{ID} = :id and {KINDERGARTEN_ID} = :kindergarten_id',
            ExpressionAttributeValues={':id': child_id, ':kindergarten_id': kindergarten_id},
            Limit=1
        )
        return response['Count'] >= 1