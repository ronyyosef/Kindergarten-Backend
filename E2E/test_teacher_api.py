import json

import pytest
from uuid import UUID

from E2E.API.child.add_child import add_child_api
from E2E.API.child.get_child import get_child_api
from E2E.API.teacher.get_teacher import get_teacher_api
from E2E.API.teacher.update_teacher import update_teacher_api
from E2E.API.teacher.update_teacher_name import update_teacher_name_api
from shared.hanlders.KindergartenHandler import KindergartenHandler
from shared.hanlders.TeacherHandler import TeacherHandler


def setup_module():
    pass


def teardown_module():
    pass


@pytest.mark.dependency(name="create_teacher")
def test_update_teacher_create_new_kindergarten(auth):
    response = update_teacher_api(
        token=auth.token,
        first_name='e2e_first_name',
        last_name='e2e_last_name',
        kindergarten_id=None,
        kindergarten_name='e2e_kindergarten_name')
    assert response.status_code == 200
    response = get_teacher_api(token=auth.token)
    data = json.loads(response.text)
    assert data['last_name'] == 'e2e_last_name'
    assert data['kindergarten_id'] is not None
    assert data['first_name'] == 'e2e_first_name'
    assert data['teacher_id'] == auth.teacher_id
    assert data['group_name'] == 'קבוצה ראשית'
    assert data['photo_link'] is None


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
    assert response.status_code == 200
    response = get_teacher_api(token=auth.token)
    data = json.loads(response.text)
    assert data['last_name'] == 'e2e_last_name'
    assert data['kindergarten_id'] == kindergarten_id
    assert data['first_name'] == 'e2e_first_name'
    assert data['teacher_id'] == auth.teacher_id
    assert data['group_name'] == 'קבוצה ראשית'
    assert data['photo_link'] is None


def test_update_teacher_change_first_name_last_name(auth):
    response = update_teacher_api(
        token=auth.token,
        first_name='e2e_first_name',
        last_name='e2e_last_name',
        kindergarten_id=None,
        kindergarten_name='e2e_kindergarten_name')
    assert response.status_code == 200

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


def test_update_teacher_change_group_name(auth):
    pass


# Child
def test_add_child(auth):
    response = add_child_api(
        token=auth.token,
        first_name='test_first_name',
        last_name='test_last_name',
        parent1_phone_number='123',
        parent2_phone_number='456',
        group_name='123')
    assert response.status_code == 200
    data_child_create = json.loads(response.text)
    response = get_child_api(auth.token,
                             child_id=data_child_create['id_created'])
    child_data = json.loads(response.text)
    assert child_data['child_id'] == data_child_create['id_created']
    assert child_data['last_name'] == 'test_last_name'
    assert child_data['first_name'] == 'test_first_name'
    assert child_data['parent1_phone_number'] == '123'
    assert child_data['parent2_phone_number'] == '456'
    assert child_data['group_name'] == '123'
