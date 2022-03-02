from datetime import date

from const import ID
from shared.AttendanceHandler import AttendanceHandler
from shared.ChildrenHandler import ChildrenHandler
from shared.CognitoHandler import CognitoHandler
from shared.TeacherHandler import TeacherHandler


def get_kindergarten_children(event, context):
    user = CognitoHandler.get_user_id(event)
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(user)
    children = ChildrenHandler.get_children_for_kindergarten(kindergarten_id)
    for child in children:
        attend_status = AttendanceHandler.get_attendance(child_id=child.get(ID), date_query=str(date.today()))
        child['is_present'] = attend_status

    return children
