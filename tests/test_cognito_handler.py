from shared.CognitoHandler import CognitoHandler
from tests.shared import event_mock


def setup_module():
    pass


def teardown_module():
    pass


def test_cognitoHandler():
    user = CognitoHandler.get_user_id(event_mock)
    assert user == '+972532840340'

