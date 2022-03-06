import logging
import random

from const import KINDERGARTEN_ID, FIRST_NAME, LAST_NAME, PARENT1_PHONE_NUMBER, PARENT2_PHONE_NUMBER, PHOTO_LINK, \
    GROUP_NUMBER, ID
from shared.ChildrenHandler import ChildrenHandler
from shared.CognitoHandler import CognitoHandler
from shared.TeacherHandler import TeacherHandler
from utils.logger import logger
from utils.random import get_random_id


def add_child_data(event, context):
    id_for_added_child = "-1"
    user = CognitoHandler.get_user_id(event)

    id_is_in_use = True
    while id_is_in_use:
        id_for_added_child = get_random_id()
        id_is_in_use = ChildrenHandler.check_if_key_exists(id_for_added_child)
    logger.info(f"id to be used {id_for_added_child}")
    teacher_data = TeacherHandler.get_teacher_data(user)
    body: dict = event['customBody']
    child_to_add = {
        ID: id_for_added_child,
        KINDERGARTEN_ID: teacher_data[KINDERGARTEN_ID],
        FIRST_NAME: body.get(FIRST_NAME, None),
        LAST_NAME: body.get(LAST_NAME, None),
        GROUP_NUMBER: teacher_data[GROUP_NUMBER],
        PARENT1_PHONE_NUMBER: body.get(PARENT1_PHONE_NUMBER, None),
        PARENT2_PHONE_NUMBER: body.get(PARENT2_PHONE_NUMBER, None),
    }

    logger.info(f"child to be added is :{child_to_add}")
    ChildrenHandler.add_child(**child_to_add)
    return {"code": "200", "message": "Child updated successfully", "id_created": id_for_added_child}
