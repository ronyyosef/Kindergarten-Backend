from const import ID, TEACHER_ID
from shared.AttendanceHandler import AttendanceHandler
from shared.ChildrenHandler import ChildrenHandler
from shared.TeacherHandler import TeacherHandler
from shared.lambda_decorator import lambda_decorator


@lambda_decorator
def add_attendance_data(event, context):
    child_id: str = event['customBody'][ID]
    is_present: bool = event['customBody']['is_present']
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(event[TEACHER_ID])

    if not ChildrenHandler.child_in_kindergarten(child_id, kindergarten_id):
        return 'child not exist/ child not in this kindergarten'

    if is_present:
        AttendanceHandler.add_attendance(child_id=child_id, kindergarten_id=kindergarten_id)
    else:
        AttendanceHandler.remove_attendance(child_id=child_id)
