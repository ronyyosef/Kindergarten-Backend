import logging
import random

from const import KINDERGARTEN_ID, FIRST_NAME, LAST_NAME, PARENT1_PHONE_NUMBER, PARENT2_PHONE_NUMBER, PHOTO_LINK, \
    GROUP_NUMBER, ID
from shared.ChildrenHandler import ChildrenHandler
from utils.logger import logger
from utils.random import get_random_id


def add_child_data(event, context):
    logger.info(f"Event: {event}")
    id_for_added_child = "-1"

    id_is_in_use = True
    while id_is_in_use:
        id_for_added_child = get_random_id()
        id_is_in_use = ChildrenHandler.check_if_key_exists(id_for_added_child)
    logger.info(f"id tobe used {id_for_added_child}")

    body: dict = event['customBody']
    child_to_add = {
        ID: id_is_in_use,
        KINDERGARTEN_ID: body.get(KINDERGARTEN_ID, None),
        FIRST_NAME: body.get(FIRST_NAME, None),
        LAST_NAME: body.get(LAST_NAME, None),
        PHOTO_LINK: body.get(PHOTO_LINK, None),
        GROUP_NUMBER: body.get(GROUP_NUMBER, None),
        PARENT1_PHONE_NUMBER: body.get(PARENT1_PHONE_NUMBER, None),
        PARENT2_PHONE_NUMBER: body.get(PARENT2_PHONE_NUMBER, None),
    }

    logger.info(f"child to be added is :{child_to_add}")
    ChildrenHandler.add_child(**child_to_add)
    return {"code": "200", "message": f"Child updated successfully with id {id_for_added_child}"}
