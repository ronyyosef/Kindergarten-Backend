import boto3

from const import KINDERGARTEN_TABLE

teacher_table = boto3.resource('dynamodb').Table(KINDERGARTEN_TABLE)


class KindergartenHandler:

    @staticmethod
    def add_kindergarten():
        pass

    @staticmethod
    def get_kindergarten():
        pass

    @staticmethod
    def update_kindergarten():
        pass

    @staticmethod
    def delete_kindergarten(phone_number):
        pass
