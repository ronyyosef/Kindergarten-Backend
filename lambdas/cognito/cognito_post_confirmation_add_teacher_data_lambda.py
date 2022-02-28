
from shared.TeacherHandler import TeacherHandler
from utils.logger import logger

event = {'version': '1', 'region': 'us-east-1', 'userPoolId': 'us-east-1_PokjeshX3',
         'userName': '1da35496-4f62-49a7-a798-102764bd645d',
         'callerContext': {'awsSdkVersion': 'aws-sdk-unknown-unknown', 'clientId': '36d8opu7j2e9illge6vlfjdu9h'},
         'triggerSource': 'PostConfirmation_ConfirmSignUp', 'request': {
        'userAttributes': {'sub': '1da35496-4f62-49a7-a798-102764bd645d', 'cognito:user_status': 'CONFIRMED',
                           'cognito:phone_number_alias': '+972532840340', 'phone_number_verified': 'false',
                           'phone_number': '+972532840340'}}, 'response': {}}

def add_teacher_data(event, context):
    phone_number = event['request']['userAttributes']['phone_number']
    logger.info(f'Adding new teacher phone number = {phone_number}')
    TeacherHandler.add_teacher(phone_number=phone_number)
    return event
