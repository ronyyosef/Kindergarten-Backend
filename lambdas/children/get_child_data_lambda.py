import logging

from const import ID, FIRST_NAME, LAST_NAME, PHOTO_LINK, GROUP_NUMBER, KINDERGARTEN_ID
from shared.ChildrenHandler import ChildrenHandler


def get_child_data(event, context):
    response = ChildrenHandler.get_child(event["querystring"]["id"])
    return response
