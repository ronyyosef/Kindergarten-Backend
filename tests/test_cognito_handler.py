from shared.hanlders.CognitoHandler import CognitoHandler
from tests.shared import event_mock


def setup_module():
    pass


def teardown_module():
    pass


def test_cognitoHandler():
    teacher_id = CognitoHandler.get_teacher_id(event_mock)
    assert teacher_id == '74b835f4-775c-4c41-bea6-5a77b624e7dd'
