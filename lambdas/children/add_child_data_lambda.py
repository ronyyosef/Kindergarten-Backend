import logging

from shared.ChildrenHandler import ChildrenHandler
from utils.logger import logger


def add_child_data(event, context):
    logger.info(f"Event: {event}")
    return_message = None

    if 'querystring' in event:
        try:
            ChildrenHandler.add_child(**event["querystring"])
            return_message = "Child was added successfully"
        except Exception as err:
            logger.error(str(err))
            return_message = err

    return return_message
