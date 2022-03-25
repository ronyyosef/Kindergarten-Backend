from datetime import date

from shared.const import TEACHER_ID, CHILD_ID, GROUP_NAME, KINDERGARTEN_ID
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_kindergarten_children(event, context):
    teacher_data = TeacherHandler.get_teacher_data(
        event[TEACHER_ID])
    children = ChildrenHandler.get_children_for_kindergarten_and_group(
        teacher_data[KINDERGARTEN_ID], teacher_data[GROUP_NAME])
    for child in children:
        attend_status = AttendanceHandler.get_attendance(
            child_id=child.get(CHILD_ID), date_query=str(date.today()))
        if attend_status:
            child['is_present'] = attend_status["is_present"]
        else:
            child['is_present'] = "no"
    return children
