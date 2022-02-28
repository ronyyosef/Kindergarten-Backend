
from shared.ChildrenHandler import ChildrenHandler


def get_child_data(event, context):
    response = ChildrenHandler.get_child(event["querystring"]["id"])
    return response
