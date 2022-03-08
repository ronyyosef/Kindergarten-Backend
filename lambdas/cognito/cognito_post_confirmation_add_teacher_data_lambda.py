from const import PHONE_NUMBER
from shared.TeacherHandler import TeacherHandler
from shared.slack_notification import send_new_user_msg

# event = {
#     'version': '1',
#     'region': 'us-east-1',
#     'userPoolId': 'xxxxxxxxx',
#     'userName': 'xxxxxxxxxxxxxxxxx',
#     'callerContext': {'awsSdkVersion': 'aws-sdk-unknown-unknown', 'clientId': 'xxxxxxxxxxxx'},
#     'triggerSource': 'PostConfirmation_ConfirmSignUp',
#     'request': {
#         'userAttributes':
#             {'sub': 'xxxxxxxxxxxxxxxxxx',
#              'cognito:user_status': 'CONFIRMED',
#              'cognito:phone_number_alias': 'XXXXXXXXXXX',
#              'phone_number_verified': 'false',
#              'phone_number': 'XXXXXXXXX'}}, 'response': {}}


def add_teacher_data(event, context):
    teacher_id = event['userName']
    phone_number = event['request']['userAttributes'][PHONE_NUMBER]
    TeacherHandler.add_teacher(teacher_id=teacher_id, phone_number=phone_number)
    send_new_user_msg(f"New user register, phone number: {phone_number}")
    return event
