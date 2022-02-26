import logging

from shared.ChildrenHandler import ChildrenHandler


def add_child_data(event, context):
    logging.info(f"Event: {event}")

    if 'querystring' in event:
        try:
            ChildrenHandler.add_child(**event["querystring"])
            return_message = "Child was added successfully"
        except Exception as err:
            return_message = err

    return return_message


