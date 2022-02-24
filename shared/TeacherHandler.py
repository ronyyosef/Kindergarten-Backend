import logging

import boto3

from const import TEACHERS_TABLE, PHONE_NUMBER, FIRST_NAME, LAST_NAME, PHOTO_LINK, KINDERGARTEN_ID, GROUP_NUMBER, EMAIL, \
    IS_ADMIN


class TeacherHandler:

    @staticmethod
    def add_teacher(phone_number, first_name, last_name, photo_link, kindergarten_id, group_number, email, is_admin):
        teacher_table = boto3.resource('dynamodb').Table(TEACHERS_TABLE)

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
            teacher_table.put_item(Item=new_teacher)
        except Exception as e:
            logging.error(f'Cannot put {new_teacher} in {TEACHERS_TABLE}, {str(e)}')

    @staticmethod
    def update_teacher(phone_number, first_name, last_name, photo_link, kindergarten_id, group_number, email, is_admin):
        teacher_table = boto3.resource('dynamodb').Table(TEACHERS_TABLE)

        teacher_update_info = {
            PHONE_NUMBER: phone_number,
            FIRST_NAME: first_name,
            LAST_NAME: last_name,
            PHOTO_LINK: photo_link,
            KINDERGARTEN_ID: kindergarten_id,
            GROUP_NUMBER: group_number,
            IS_ADMIN: is_admin
        }
        try:

            response = teacher_table.update_item(
                Key={
                    PHONE_NUMBER: phone_number,
                },
                AttributeUpdates={
                    FIRST_NAME: first_name,
                    LAST_NAME: last_name,
                    PHOTO_LINK: photo_link,
                    KINDERGARTEN_ID: kindergarten_id,
                    GROUP_NUMBER: group_number,
                    IS_ADMIN: is_admin
                },
            )
            return response



        except Exception as e:
            logging.error(f'Cannot put {teacher_update_info} in {TEACHERS_TABLE}, {str(e)}')
