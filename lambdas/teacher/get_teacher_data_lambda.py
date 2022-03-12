import logging

from shared.const import TEACHER_ID
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_teacher_data(event, context):
    teacher_data = TeacherHandler.get_teacher_data(event[TEACHER_ID])
    logging.info(f'Teacher data : {teacher_data}')
    return teacher_data
