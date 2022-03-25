import boto3
from boto3.dynamodb.conditions import Key

from shared.const import KINDERGARTEN_ID, GROUPS_TABLE, GROUP_NAME

groups_table = boto3.resource('dynamodb').Table(GROUPS_TABLE)


class GroupsHandler:

    @staticmethod
    def get_kindergarten_groups(kindergarten_id: str):
        response = groups_table.query(KeyConditionExpression=Key(
            KINDERGARTEN_ID).eq(kindergarten_id))
        groups_in_kindergarten = []
        for group in response['Items']:
            groups_in_kindergarten.append(group["group_name"])
        return {'groups_in_kindergarten': groups_in_kindergarten}

    @staticmethod
    def add_group_to_kindergarten(kindergarten_id: str, group_name: str):
        new_group = {
            KINDERGARTEN_ID: kindergarten_id,
            GROUP_NAME: group_name
        }
        groups_table.put_item(Item=new_group)

    @staticmethod
    def delete_group_from_kindergarten(kindergarten_id, group_name_to_delete):
        response = groups_table.delete_item(
            Key={
                KINDERGARTEN_ID: kindergarten_id,
                GROUP_NAME: group_name_to_delete
            })
        return response
