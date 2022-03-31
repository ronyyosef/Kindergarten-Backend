import uuid

from shared.const import KINDERGARTEN_ID, FIRST_NAME, LAST_NAME, \
    PARENT1_PHONE_NUMBER, PARENT2_PHONE_NUMBER, \
    GROUP_NAME, TEACHER_ID, CHILD_ID, EVENT_BODY
from shared.error_handling.error_codes import INPUT_ERROR
from shared.error_handling.exception import MyException
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.GroupsHandler import GroupsHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator
from utils.logger import logger


@lambda_decorator
def add_child_data(event, context):
    new_child_id = str(uuid.uuid4())
    teacher_data = TeacherHandler.get_teacher_data(event[TEACHER_ID])
    body: dict = event[EVENT_BODY]
    group_name = body.get(
        GROUP_NAME,
        teacher_data[GROUP_NAME])
    if GroupsHandler.group_exist(
            kindergarten_id=teacher_data[KINDERGARTEN_ID],
            group_name=group_name) is False:
        raise MyException("group_name does not exist", INPUT_ERROR)
    child_to_add = {
        CHILD_ID: new_child_id,
        KINDERGARTEN_ID: teacher_data[KINDERGARTEN_ID],
        FIRST_NAME: body.get(FIRST_NAME, None),
        LAST_NAME: body.get(LAST_NAME, None),
        GROUP_NAME: body.get(GROUP_NAME, teacher_data[GROUP_NAME]),
        PARENT1_PHONE_NUMBER: body.get(PARENT1_PHONE_NUMBER, None),
        PARENT2_PHONE_NUMBER: body.get(PARENT2_PHONE_NUMBER, None),
    }

    logger.info(f"child to be added is :{child_to_add}")
    ChildrenHandler.add_child(**child_to_add)
    return {"code": "200", "message": "Child updated successfully",
            "id_created": new_child_id}
