import uuid

from const import KINDERGARTEN_ID, FIRST_NAME, LAST_NAME, PARENT1_PHONE_NUMBER, PARENT2_PHONE_NUMBER, PHOTO_LINK, \
    GROUP_NUMBER, TEACHER_ID, CHILD_ID
from shared.ChildrenHandler import ChildrenHandler
from shared.TeacherHandler import TeacherHandler
from shared.lambda_decorator import lambda_decorator
from utils.logger import logger


@lambda_decorator
def add_child_data(event, context):
    new_child_id = str(uuid.uuid4())
    teacher_data = TeacherHandler.get_teacher_data(event[TEACHER_ID])
    body: dict = event['customBody']
    child_to_add = {
        CHILD_ID: new_child_id,
        KINDERGARTEN_ID: teacher_data[KINDERGARTEN_ID],
        FIRST_NAME: body.get(FIRST_NAME, None),
        LAST_NAME: body.get(LAST_NAME, None),
        GROUP_NUMBER: teacher_data[GROUP_NUMBER],
        PARENT1_PHONE_NUMBER: body.get(PARENT1_PHONE_NUMBER, None),
        PARENT2_PHONE_NUMBER: body.get(PARENT2_PHONE_NUMBER, None),
    }

    logger.info(f"child to be added is :{child_to_add}")
    ChildrenHandler.add_child(**child_to_add)
    return {"code": "200", "message": "Child updated successfully", "id_created": new_child_id}
