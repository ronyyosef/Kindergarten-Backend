import logging

from shared.const import PHONE_NUMBER, CHILD_ID, KINDERGARTEN_ID
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.ParendHandler import ParentHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.slack_notification import send_new_user_msg


# event = { 'version': '1', 'region': 'us-east-1', 'userPoolId': 'xxxix',
# 'userName': 'xxxxxxxxxxxxxxxxx', 'callerContext': {'awsSdkVersion':
# 'aws-sdk-unknown-unknown', 'clientId': 'xxxxxxxxxxxx'}, 'triggerSource':
# 'PostConfirmation_ConfirmSignUp', 'request': { 'userAttributes': {'sub':
# 'xxxxxxxxxxxxxxxxxx', 'cognito:user_status': 'CONFIRMED',
# 'cognito:phone_number_alias': 'XXXXXXXXXXX', 'phone_number_verified':
# 'false', 'phone_number': 'XXXXXXXXX'}}, 'response': {}}


def add_teacher_or_parent(event, context):
    user_id = event['userName']
    phone_number = event['request']['userAttributes'][PHONE_NUMBER]
    child = ChildrenHandler.get_child_by_parent_number(phone_number)
    if child is None:
        TeacherHandler.add_teacher(
            teacher_id=user_id, phone_number=phone_number)
        send_new_user_msg(
            f"New Teacher register, phone number: {phone_number}")
    else:
        logging.info(f'child_data: {child}')
        ParentHandler.add_parent(
            parent_id=user_id,
            phone_number=phone_number,
            child_id=child[CHILD_ID],
            kindergarten_id=child[KINDERGARTEN_ID])
        send_new_user_msg(f"New Parent register, phone number: {phone_number}")
    return event
