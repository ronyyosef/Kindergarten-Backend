from shared.KindergartenHandler import KindergartenHandler


def setup_module():
    pass


def teardown_module():
    pass


def test_KindergartenHandler():
    response = KindergartenHandler.add_kindergarten('123','name')
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200

    response = KindergartenHandler.get_kindergarten('123')
    # response = TeacherHandler.get_teacher_data('test_phone_number')
    # assert response == {'last_name': None, 'is_admin': None, 'group_number': None, 'kindergarten_id': None,
    #                     'photo_link': None, 'first_name': None, 'phone_number': 'test_phone_number'}
    # response = TeacherHandler.update_teacher('test_phone_number', 'Rony', 'Yosef', 'photo_link', 'kindlergaten_id', '0',
    #                                          'yes')
    # assert response == {'last_name': 'Yosef', 'group_number': '0', 'is_admin': 'yes',
    #                     'kindergarten_id': 'kindlergaten_id', 'first_name': 'Rony', 'photo_link': 'photo_link',
    #                     'phone_number': 'test_phone_number'}
    #
    # response = TeacherHandler.delete_teacher('test_phone_number')
    # assert response['ResponseMetadata']['HTTPStatusCode'] == 200
