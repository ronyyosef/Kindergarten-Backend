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
def update_child_group_name(event, context):
    teacher_id = event[TEACHER_ID]
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(teacher_id)
    body = event[EVENT_BODY]
    child_id = body.get(CHILD_ID, None)
    group_name = body.get(GROUP_NAME, None)
    if child_id is not None and group_name is not None:
        ChildrenHandler.update_child_group_name(child_id=child_id,
                                                kindergarten_id=kindergarten_id,
                                                group_name=group_name)
    else:
        return "parameter is missing"
