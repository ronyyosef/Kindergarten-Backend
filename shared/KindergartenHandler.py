import boto3
from boto3.dynamodb.conditions import Key

from utils.logger import logger
from const import KINDERGARTEN_TABLE, KINDERGARTEN_NAME, KINDERGARTEN_ID

kindergarten_table = boto3.resource('dynamodb').Table(KINDERGARTEN_TABLE)


class KindergartenHandler:

    @staticmethod
    def add_kindergarten(kindergarten_id: str, kindergarten_name: str) -> None:

        new_kindergarten = {
            KINDERGARTEN_ID: kindergarten_id,
            KINDERGARTEN_NAME: kindergarten_name
        }

        try:
            kindergarten_table.put_item(Item=new_kindergarten)
        except Exception as e:
            logger.error(f'Cannot put {new_kindergarten} in {KINDERGARTEN_TABLE}, {str(e)}')

    @staticmethod
    def get_kindergarten(kindergarten_id: str) -> dict:
        try:
            logger.info(f'Trying to get kindergarten: {kindergarten_id}')
            response = kindergarten_table.query(KeyConditionExpression=Key(KINDERGARTEN_ID).eq(kindergarten_id), Limit=1)
            kindergarten_data = response["Items"][0] if response['Count'] == 1 else None
            return kindergarten_data
        except Exception as e:
            logger.error(f'Error: { str(e)}')

    @staticmethod
    def update_kindergarten():
        pass

    @staticmethod
    def delete_kindergarten():
        pass

    @staticmethod
    def check_if_kindergarten_exists(kindergarten_id: str) -> bool:
        response = kindergarten_table.query(
            KeyConditionExpression=Key(KINDERGARTEN_ID).eq(kindergarten_id))
        return len(response["Items"]) > 0
