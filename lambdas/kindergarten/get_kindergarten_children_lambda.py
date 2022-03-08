from datetime import date

from const import TEACHER_ID, CHILD_ID
from shared.AttendanceHandler import AttendanceHandler
from shared.ChildrenHandler import ChildrenHandler
from shared.TeacherHandler import TeacherHandler
from shared.lambda_decorator import lambda_decorator


@lambda_decorator
def get_kindergarten_children(event, context):
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(event[TEACHER_ID])
    children = ChildrenHandler.get_children_for_kindergarten(kindergarten_id)
    for child in children:
        attend_status = AttendanceHandler.get_attendance(child_id=child.get(CHILD_ID), date_query=str(date.today()))
        child['is_present'] = attend_status

    return children
