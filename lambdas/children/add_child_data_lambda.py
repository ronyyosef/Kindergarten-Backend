import logging
import random

from shared.ChildrenHandler import ChildrenHandler
from utils.logger import logger
from utils.random import get_random_id


def add_child_data(event, context):
    logger.info(f"Event: {event}")
    return_message = "customBody parameter is missing"
    id_for_added_child = "-1"

    id_is_in_use = True
    while id_is_in_use:
        id_for_added_child = get_random_id()
        id_is_in_use = ChildrenHandler.check_if_key_exists(id_for_added_child)

    if 'customBody' in event:
        try:
            ChildrenHandler.add_child(id=id_for_added_child, **event["customBody"])
            return_message = {"code": "200", "message": "Child updated successfully"}
        except Exception as err:
            logger.error(str(err))
            return_message = err

    return return_message
