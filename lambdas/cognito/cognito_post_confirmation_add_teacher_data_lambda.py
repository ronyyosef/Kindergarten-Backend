
from shared.TeacherHandler import TeacherHandler
from shared.slack_notification import send_new_user_msg
from utils.logger import logger


def add_teacher_data(event, context):
    phone_number = event['request']['userAttributes']['phone_number']
    logger.info(f'Adding new teacher phone number = {phone_number}')
    TeacherHandler.add_teacher(phone_number=phone_number)
    send_new_user_msg(f"New user register {phone_number}")
    return event
