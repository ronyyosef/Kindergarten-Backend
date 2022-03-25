import uuid

from shared.const import KINDERGARTEN_ID, FIRST_NAME, LAST_NAME, \
    PARENT1_PHONE_NUMBER, PARENT2_PHONE_NUMBER, \
    GROUP_NAME, TEACHER_ID, CHILD_ID, EVENT_BODY
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.GroupsHandler import GroupsHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator
from utils.logger import logger


@lambda_decorator
def update_teacher_group_name(event, context):
    teacher_id = event[TEACHER_ID]
    teacher_data = TeacherHandler.get_teacher_data(teacher_id)
    body = event[EVENT_BODY]
    group_name = body.get(GROUP_NAME, None)
    if group_name is not None:
        TeacherHandler.update_teacher_group_name(
            teacher_data=teacher_data,
            group_name=group_name)
    else:
        return "parameter is missing"
