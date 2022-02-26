
from shared.CognitoHandler import CognitoHandler
from shared.TeacherHandler import TeacherHandler
from utils.logger import logger


def get_teacher_data(event, context):
    teacher_id = CognitoHandler.get_user_id(event)
    teacher_data = TeacherHandler.get_teacher_data(teacher_id)
    logger.info(f'Teacher data : {teacher_data}')
    return teacher_data
