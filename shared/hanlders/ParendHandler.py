import boto3

from shared.const import PARENT_TABLE, KINDERGARTEN_ID, CHILD_ID, PARENT_ID, PHONE_NUMBER

child_table = boto3.resource('dynamodb').Table(PARENT_TABLE)


class ParentHandler:
    @staticmethod
    def add_parent(
            parent_id: str,
            phone_number: str,
            child_id: str,
            kindergarten_id: str):

        new_child = {
            PARENT_ID: parent_id,
            PHONE_NUMBER: phone_number,
            CHILD_ID: child_id,
            KINDERGARTEN_ID: kindergarten_id
        }
        child_table.put_item(Item=new_child)
