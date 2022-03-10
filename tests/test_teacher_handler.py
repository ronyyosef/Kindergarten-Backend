from shared.TeacherHandler import TeacherHandler


def setup_module():
    pass


def teardown_module():
    pass


def test_TeacherHandler():
    response = TeacherHandler.add_teacher(teacher_id='test_teacher_id', phone_number='test_phone_number')
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200

    response = TeacherHandler.get_teacher_data('test_teacher_id')
    assert response == {'last_name': None, 'group_number': None, 'is_admin': None, 'kindergarten_id': None,
                        'first_name': None, 'phone_number': 'test_phone_number', 'teacher_id': 'test_teacher_id',
                        'photo_link': None}
    response = TeacherHandler.update_teacher(teacher_id='test_teacher_id', first_name='fname', last_name='lname',
                                             kindergarten_id='test_kindergarten',
                                             group_number='test', is_admin='test')
    assert response == {'last_name': 'lname', 'group_number': 'test', 'is_admin': 'test',
                        'kindergarten_id': 'test_kindergarten', 'first_name': 'fname',
                        'phone_number': 'test_phone_number', 'teacher_id': 'test_teacher_id'}
    response = TeacherHandler.delete_teacher('test_teacher_id')
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200
