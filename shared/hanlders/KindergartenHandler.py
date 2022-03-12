import logging

import boto3
from boto3.dynamodb.conditions import Key

from shared.const import KINDERGARTEN_TABLE, KINDERGARTEN_NAME, KINDERGARTEN_ID

kindergarten_table = boto3.resource('dynamodb').Table(KINDERGARTEN_TABLE)


class KindergartenHandler:

    @staticmethod
    def add_kindergarten(kindergarten_id: str, kindergarten_name: str) -> None:
        new_kindergarten = {
            KINDERGARTEN_ID: kindergarten_id,
            KINDERGARTEN_NAME: kindergarten_name
        }
        kindergarten_table.put_item(Item=new_kindergarten)

    @staticmethod
    def get_kindergarten(kindergarten_id: str) -> dict:
        logging.info(f'Trying to get kindergarten: {kindergarten_id}')
        response = kindergarten_table.query(
            KeyConditionExpression=Key(KINDERGARTEN_ID).eq(kindergarten_id),
            Limit=1)
        kindergarten_data = response["Items"][0] if response[
                                                        'Count'] == 1 else None
        return kindergarten_data

    @staticmethod
    def update_kindergarten():
        pass

    @staticmethod
    def delete_kindergarten(kindergarten_id: str):
        # TODO
        pass

    @staticmethod
    def check_if_kindergarten_exists(kindergarten_id: str) -> bool:
        response = kindergarten_table.query(
            KeyConditionExpression=Key(KINDERGARTEN_ID).eq(kindergarten_id))
        return len(response["Items"]) > 0
