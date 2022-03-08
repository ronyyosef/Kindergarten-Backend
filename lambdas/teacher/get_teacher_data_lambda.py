from const import USER_ID
from shared.CognitoHandler import CognitoHandler
from shared.TeacherHandler import TeacherHandler
from shared.lambda_decorator import lambda_decorator
from utils.logger import logger


@lambda_decorator
def get_teacher_data(event, context):
    teacher_data = TeacherHandler.get_teacher_data(event[USER_ID])
    logger.info(f'Teacher data : {teacher_data}')
    return teacher_data
