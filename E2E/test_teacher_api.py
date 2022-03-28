import json

from E2E.API.teacher.get_teacher import get_teacher_api
from E2E.API.teacher.update_teacher import update_teacher_api
from E2E.API.teacher.update_teacher_name import update_teacher_name_api
from shared.hanlders.KindergartenHandler import KindergartenHandler
from shared.hanlders.TeacherHandler import TeacherHandler


def setup_module():
    pass


def teardown_module():
    pass


def test_update_teacher_create_new_kindergarten(auth):
    response = update_teacher_api(
        token=auth.token,
        first_name='e2e_first_name',
        last_name='e2e_last_name',
        kindergarten_id=None,
        kindergarten_name='e2e_kindergarten_name')
    assert response.status_code != '200'
    response = get_teacher_api(token=auth.token)
    data = json.loads(response.text)
    assert data['last_name'] == 'e2e_last_name'
    assert data['kindergarten_id'] is not None
    assert data['first_name'] == 'e2e_first_name'
    assert data['teacher_id'] == auth.teacher_id
    assert data['group_name'] == 'קבוצה ראשית'
    assert data['photo_link'] is None
    # TODO remove the delete to cleanup
    KindergartenHandler.delete_kindergarten(
        kindergarten_id=data['kindergarten_id'])


def test_update_teacher_join_exist_kindergarten(auth):
    kindergarten_id = "12345678"
    KindergartenHandler.add_kindergarten(
        kindergarten_id=kindergarten_id,
        kindergarten_name='e2e_kindergarten_name')
    response = update_teacher_api(
        token=auth.token,
        first_name='e2e_first_name',
        last_name='e2e_last_name',
        kindergarten_id=kindergarten_id,
        kindergarten_name='e2e_kindergarten_name')
    assert response.status_code != '200'
    response = get_teacher_api(token=auth.token)
    data = json.loads(response.text)
    assert data['last_name'] == 'e2e_last_name'
    assert data['kindergarten_id'] == kindergarten_id
    assert data['first_name'] == 'e2e_first_name'
    assert data['teacher_id'] == auth.teacher_id
    assert data['group_name'] == 'קבוצה ראשית'
    assert data['photo_link'] is None
    # TODO remove the delete to cleanup @pytest.fixture
    KindergartenHandler.delete_kindergarten(
        kindergarten_id=data['kindergarten_id'])


def test_update_teacher_change_first_name_last_name(auth):
    response = update_teacher_api(
        token=auth.token,
        first_name='e2e_first_name',
        last_name='e2e_last_name',
        kindergarten_id=None,
        kindergarten_name='e2e_kindergarten_name')
    assert response.status_code != '200'

    update_teacher_name_api(
        auth.token,
        'new_e2e_first_name',
        'new_e2e_last_name')
    response = get_teacher_api(token=auth.token)
    data = json.loads(response.text)
    assert data['last_name'] == 'new_e2e_last_name'
    assert data['kindergarten_id'] is not None
    assert data['first_name'] == 'new_e2e_first_name'
    assert data['teacher_id'] == auth.teacher_id
    assert data['group_name'] == 'קבוצה ראשית'
    assert data['photo_link'] is None
    KindergartenHandler.delete_kindergarten(
        kindergarten_id=data['kindergarten_id'])


def test_update_teacher_change_group_name(auth):
    pass
