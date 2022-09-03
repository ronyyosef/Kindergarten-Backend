import datetime

from pydantic import BaseModel, Field, root_validator
from shared.const import TEACHER_ID, CHILD_ID, DATE, KINDERGARTEN_ID, TIME_OUT, \
    TIME_IN, IS_PRESENT, EVENT_BODY, ID
from shared.error_handling.error_codes import INPUT_ERROR
from shared.error_handling.exception import MyException
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.ParentHandler import ParentHandler
from shared.hanlders.TeacherHandler import TeacherHandler

from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def add_child_attendance(event, context):
    # This api is called for both parent and teacher in calender component.
    is_parent = False
    is_teacher = False
    teacher_id = event[TEACHER_ID]
    event_body = event[EVENT_BODY]
    is_present = event_body["is_present"]
    child_id = event_body["id"]
    attendance_date = event_body["attendance_date"]
    parent_data = ParentHandler.get_parent_data(teacher_id)
    if parent_data.get('Item') is None:
        kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(teacher_id)
        is_teacher = True
    else:
        kindergarten_id = parent_data.get('Item')[KINDERGARTEN_ID]
        is_parent = True

    child_attendance = AttendanceHandler.get_attendance(child_id=child_id, date_query=attendance_date)
    attendance_exists = True if child_attendance is not None else False

    if attendance_exists:
        if is_present == "no":
            if child_attendance["is_present"] == "yes" and is_parent:
                raise Exception("Error, You cannot delete a child attendance if child had attended")
            else:
                AttendanceHandler.delete_attendance(child_id=child_id, date_query=attendance_date)
        elif is_present == "notified_missing":
            AttendanceHandler.update_attendance(child_id=child_id, kindergarten_id=kindergarten_id,
                                                is_present="notified_missing", date_query=attendance_date)
    else:
        if is_present == "no":
            pass
        elif is_present == "notified_missing":
            AttendanceHandler.add_attendance(child_id=child_id, kindergarten_id=kindergarten_id,
                                             is_present="notified_missing", date_query=attendance_date)
        elif is_present == "yes" and is_teacher:
            AttendanceHandler.add_attendance(child_id=child_id, kindergarten_id=kindergarten_id,
                                             is_present="yes")
