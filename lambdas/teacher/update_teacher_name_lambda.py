import logging

from shared.const import TEACHER_ID, FIRST_NAME, LAST_NAME
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def update_teacher_name(event, context):
    first_name = event.get('customBody').get(FIRST_NAME, None)
    last_name = event.get('customBody').get(LAST_NAME, None)
    updated_data = TeacherHandler.update_teacher_name(
        teacher_id=event[TEACHER_ID], first_name=first_name,
        last_name=last_name)
    return updated_data
