from datetime import date

from shared.const import TEACHER_ID, CHILD_ID
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_kindergarten_children(event, context):
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(event[TEACHER_ID])
    children = ChildrenHandler.get_children_for_kindergarten(kindergarten_id)
    for child in children:
        attend_status = AttendanceHandler.get_attendance(child_id=child.get(CHILD_ID), date_query=str(date.today()))
        if attend_status and "time_in" in child and "time_out" not in child:
            child['is_present'] = True
        else:
            child['is_present'] = False

    return children

