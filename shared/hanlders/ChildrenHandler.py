from typing import List

import boto3
from boto3.dynamodb.conditions import Key

from shared.const import CHILD_TABLE, KINDERGARTEN_ID, FIRST_NAME, LAST_NAME, \
    GROUP_NAME, PARENT1_PHONE_NUMBER, PARENT2_PHONE_NUMBER, PHOTO_LINK, \
    CHILD_ID
from shared.hanlders.S3PhotosHandler import S3PhotosHandler

child_table = boto3.resource('dynamodb').Table(CHILD_TABLE)


class ChildrenHandler:
    @staticmethod
    def add_child(
            child_id: str,
            kindergarten_id: str,
            first_name: str,
            last_name: str,
            group_name: str,
            parent1_phone_number: str,
            parent2_phone_number: str = None) -> None:
        new_child = {
            CHILD_ID: child_id,
            KINDERGARTEN_ID: kindergarten_id,
            FIRST_NAME: first_name,
            LAST_NAME: last_name,
            GROUP_NAME: group_name,
            PARENT1_PHONE_NUMBER: parent1_phone_number,
            PARENT2_PHONE_NUMBER: parent2_phone_number,
        }
        child_table.put_item(Item=new_child)

    @staticmethod
    def get_child(child_id: str) -> dict:
        response = child_table.query(
            KeyConditionExpression=Key(CHILD_ID).eq(child_id))
        if len(response['Items']) > 0:
            result = response['Items'][0]
            photo_url = S3PhotosHandler.get_photo_url(
                result[KINDERGARTEN_ID], child_id)
            result[PHOTO_LINK] = photo_url
        else:
            result = None
        return result

    @staticmethod
    def check_if_key_exists(child_id: str) -> bool:
        response = child_table.query(
            KeyConditionExpression=Key(CHILD_ID).eq(child_id))
        return len(response["Items"]) > 0

    @staticmethod
    def get_children_for_kindergarten(kindergarten_id: str) -> List[dict]:
        response = child_table.scan(
            FilterExpression=Key(KINDERGARTEN_ID).eq(kindergarten_id))
        for item in response['Items']:
            photo_url = S3PhotosHandler.get_photo_url(
                kindergarten_id, item[CHILD_ID])
            item[PHOTO_LINK] = photo_url
        return response['Items']

    @staticmethod
    def child_in_kindergarten(child_id: str, kindergarten_id: str) -> bool:
        response = child_table.query(
            KeyConditionExpression=f'{CHILD_ID} = :child_id and {KINDERGARTEN_ID} = :kindergarten_id',
            ExpressionAttributeValues={
                ':child_id': child_id,
                ':kindergarten_id': kindergarten_id},
            Limit=1)
        return response['Count'] >= 1

    @staticmethod
    def delete_child(child_id: str, kindergarten_id: str):
        response = child_table.delete_item(
            Key={
                CHILD_ID: child_id,
                KINDERGARTEN_ID: kindergarten_id
            })
        return response
