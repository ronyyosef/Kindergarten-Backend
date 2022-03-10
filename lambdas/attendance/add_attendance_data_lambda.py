import datetime

from shared.const import TEACHER_ID
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def add_attendance_data(event, context, date_query=None):
    child_id: str = event['customBody']['id']
    # is_present: bool = event['customBody']['is_present']
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(event[TEACHER_ID])

    if not ChildrenHandler.child_in_kindergarten(child_id, kindergarten_id):
        return 'child not exist/ child not in this kindergarten'

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = str(datetime.date.today())
    if AttendanceHandler.check_if_attendance_exists(child_id=child_id) is False:
        AttendanceHandler.add_attendance(child_id=child_id, kindergarten_id=kindergarten_id, time_in=current_time)
    else:
        AttendanceHandler.update_attendance(child_id=child_id, date_query=current_date, kindergarten_id=kindergarten_id,
                                            time_out=current_time)
