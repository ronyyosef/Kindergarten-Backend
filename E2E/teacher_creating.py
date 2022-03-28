import json

from E2E.API.teacher.get_teacher import get_teacher_api
from E2E.API.teacher.update_teacher import update_teacher_api
from shared.hanlders.TeacherHandler import TeacherHandler

def setup_module():
    pass


def teardown_module(auth):
    TeacherHandler.delete_teacher(auth.teacher_id)


def test_update_teacher_create_new_kindergarten(auth):
    response = update_teacher_api(token=auth.token, first_name='e2e_first_name',
                                  last_name='e2e_last_name',
                                  kindergarten_id=None,
                                  kindergarten_name='e2e_kindergarten_name')
    assert response.status_code != '200'
    response = get_teacher_api(token=auth.token)
    data = json.loads(response.text)
    assert data['last_name'] == 'e2e_last_name'
    assert data['kindergarten_id'] is not None
    assert data['first_name'] == 'e2e_first_name'
    assert data['phone_number'] == '+972999999999'
    assert data['teacher_id'] is not None
    assert data['group_name'] == 'קבוצה ראשית'
    assert data['photo_link'] is None
