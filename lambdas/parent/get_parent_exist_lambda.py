from shared.const import TEACHER_ID, KINDERGARTEN_ID, CHILD_ID, PHOTO_LINK, PHONE_NUMBER, EVENT_QUERY_STRING
from shared.hanlders.ChildrenHandler import ChildrenHandler


def get_parent_exist(event, context):
    phone_number = event[EVENT_QUERY_STRING][PHONE_NUMBER]
    child = ChildrenHandler.get_child_by_parent_number(phone_number)
    if child is None:
        return {'parent_exist': False}
    else:
        return {'parent_exist': True}
