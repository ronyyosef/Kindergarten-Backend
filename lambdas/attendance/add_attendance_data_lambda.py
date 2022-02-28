
from shared.AttendanceHandler import AttendanceHandler
from shared.CognitoHandler import CognitoHandler


def add_attendance_data(event, context):
    user = CognitoHandler.get_user_id(event)
    response = AttendanceHandler.add_attendance(child_id='test_child_id', kindergarten_id='test_kindergarten_id',
                                                has_arrived='test_has_arrived')
    return response


