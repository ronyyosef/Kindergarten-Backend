from datetime import date

from shared.hanlders.AttendanceHandler import AttendanceHandler


def setup_module():
    pass


def teardown_module():
    pass


def test_attendance_handler():
    AttendanceHandler.add_attendance(
        child_id='test_child_id', kindergarten_id='test_kindergarten_id', is_present="yes")
    response = AttendanceHandler.get_attendance(
        child_id='test_child_id', date_query=str(date.today()))
    assert response is not None

    response = AttendanceHandler.update_attendance(
        child_id='test_child_id', kindergarten_id='test_kindergarten_id', is_present="no")

    assert response is not None
    AttendanceHandler.delete_attendance(
        child_id='test_child_id', date_query=str(date.today()))
