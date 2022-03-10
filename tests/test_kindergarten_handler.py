from shared.KindergartenHandler import KindergartenHandler


def setup_module():
    pass


def teardown_module():
    pass


def test_KindergartenHandler():
    KindergartenHandler.add_kindergarten('test_id', 'name')

    response = KindergartenHandler.get_kindergarten('test_id')
    assert response == {'kindergarten_name': 'name', 'kindergarten_id': 'test_id'}