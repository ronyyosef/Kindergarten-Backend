from shared.const import PHONE_NUMBER, EVENT_QUERY_STRING, EVENT_BODY
from shared.hanlders.ChildrenHandler import ChildrenHandler


def get_parent_exist(event, context):
    phone_number = event[EVENT_BODY][PHONE_NUMBER]
    child = ChildrenHandler.get_child_by_parent_number(phone_number)
    if child is None:
        return {'parent_exist': False}
    else:
        return {'parent_exist': True}
