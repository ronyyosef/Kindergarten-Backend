import datetime

from shared.const import TEACHER_ID, CHILD_ID, DATE, KINDERGARTEN_ID, TIME_OUT, TIME_IN, IS_PRESENT
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def add_attendance_data(event, context, date_query=None):
    child_id: str = event['customBody']['id']
    is_present: bool = event['customBody']['is_present']
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(
        event[TEACHER_ID])

    if not ChildrenHandler.child_in_kindergarten(child_id, kindergarten_id):
        return 'child not exist/ child not in this kindergarten'

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = str(datetime.date.today())

    child_attendance = AttendanceHandler.get_attendance(child_id=child_id)
    if AttendanceHandler.get_attendance(child_id=child_id) is None:
        child_attendance = AttendanceHandler.add_attendance(
            child_id=child_id, kindergarten_id=kindergarten_id)

    if is_present == "yes":
        child_attendance["time_in"] = current_time
        child_attendance["is_present"] = "yes"
        child_attendance["time_out"] = None
    elif is_present == "no":
        child_attendance["time_out"] = current_time
        child_attendance["is_present"] = "no"
    elif is_present == "notified_missing":
        child_attendance["is_present"] = "no"
        child_attendance["time_in"] = None
        child_attendance["time_out"] = None
    else:
        raise Exception(f"child_attendance: {child_attendance} is not valid")

    AttendanceHandler.update_attendance(
        child_id=child_attendance.get(
            CHILD_ID, None), date_query=child_attendance.get(
            DATE, None), kindergarten_id=child_attendance.get(
                KINDERGARTEN_ID, None), time_out=child_attendance.get(
                    TIME_OUT, None), time_in=child_attendance.get(
                        TIME_IN, None), is_present=child_attendance.get(
                            IS_PRESENT, None))
