from datetime import date

from shared.AttendanceHandler import AttendanceHandler


def setup_module():
    pass


def teardown_module():
    pass


def test_AttendanceHandler():
    response = AttendanceHandler.add_attendance(child_id='test_child_id', kindergarten_id='test_kindergarten_id',
                                                has_arrived='test_has_arrived')

    assert response['ResponseMetadata']['HTTPStatusCode'] == 200

    response = AttendanceHandler.get_attendance(child_id='test_child_id', date_query=str(date.today()))
    assert response == {'child_id': 'test_child_id', 'date': '2022-02-23', 'kindergarten_id': 'test_kindergarten_id', 'has_arrived': 'test_has_arrived'}