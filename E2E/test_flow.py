from E2E.api.child.add_child import add_child_api
from E2E.api.child.delete_child import delete_child_api
from E2E.api.child.get_child import get_child_api
from E2E.api.child.update_child_group_name import update_child_group_name_api
from E2E.api.groups.add_group import add_group_api
from E2E.api.groups.delete_group import delete_group_api
from E2E.api.groups.get_kindergarten_groups import get_kindergarten_groups_api
from E2E.api.kindergarten.get_attendance_report import get_attendance_report_api
from E2E.api.kindergarten.get_kindergarten_children import \
    get_kindergarten_children_api
from E2E.api.kindergarten.get_kindergarten_exist import \
    get_kindergarten_exist_api
from E2E.api.kindergarten.get_kindergarten_info import get_kindergarten_info_api
from E2E.api.teacher.get_teacher import get_teacher_api
from E2E.api.teacher.update_teacher import update_teacher_api
from E2E.api.teacher.update_teacher_group_name import \
    update_teacher_group_name_api
from E2E.api.teacher.update_teacher_name import update_teacher_name_api
from shared.const import KINDERGARTEN_ID, KINDERGARTEN_NAME, MAIN_GROUP
from shared.hanlders.KindergartenHandler import KindergartenHandler

GROUP_NAME_2 = 'קבוצה 2'
GROUP_NAME_3 = 'קבוצה 3'


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
    assert response['statusCode'] == '200'
    response = get_teacher_api(token=auth.token)
    assert response['last_name'] == 'e2e_last_name'
    assert response['kindergarten_id'] == kindergarten_id
    assert response['first_name'] == 'e2e_first_name'
    assert response['teacher_id'] == auth.teacher_id
    assert response['group_name'] == MAIN_GROUP
    assert response['photo_link'] is None
    KindergartenHandler.delete_kindergarten(kindergarten_id=kindergarten_id)


def test_update_teacher_create_new_kindergarten(auth):
    response = update_teacher_api(
        token=auth.token,
        first_name='e2e_first_name',
        last_name='e2e_last_name',
        kindergarten_id=None,
        kindergarten_name='e2e_kindergarten_name')
    assert response['statusCode'] == '200'
    response = get_teacher_api(token=auth.token)
    assert response['last_name'] == 'e2e_last_name'
    assert response['kindergarten_id'] is not None
    assert response['first_name'] == 'e2e_first_name'
    assert response['teacher_id'] == auth.teacher_id
    assert response['group_name'] == MAIN_GROUP
    assert response['photo_link'] is None


def test_update_teacher_change_first_name_last_name(auth):
    response = update_teacher_name_api(
        auth.token,
        'new_e2e_first_name',
        'new_e2e_last_name')
    assert response['last_name'] == 'new_e2e_last_name'
    assert response['kindergarten_id'] is not None
    assert response['first_name'] == 'new_e2e_first_name'
    assert response['teacher_id'] == auth.teacher_id
    assert response['group_name'] == MAIN_GROUP


def test_add_group(auth):
    response = add_group_api(auth.token, group_name=GROUP_NAME_2)
    assert response == {'statusCode': '200'}


def test_get_kindergarten_groups(auth):
    response = get_kindergarten_groups_api(auth.token)
    assert response == {'groups_in_kindergarten': [MAIN_GROUP, GROUP_NAME_2]}


def test_delete_group(auth):
    response = add_group_api(auth.token, group_name=GROUP_NAME_3)
    assert response == {'statusCode': '200'}
    response = delete_group_api(auth.token, group_name=GROUP_NAME_3)
    assert response == {'statusCode': '200'}
    response = get_kindergarten_groups_api(auth.token)
    assert response == {'groups_in_kindergarten': [MAIN_GROUP, GROUP_NAME_2]}


def test_update_teacher_change_group_name(auth):
    response = update_teacher_group_name_api(auth.token, GROUP_NAME_2)
    assert response['statusCode'] == '200'
    response = get_teacher_api(token=auth.token)
    assert response['last_name'] == 'new_e2e_last_name'
    assert response['kindergarten_id'] is not None
    assert response['first_name'] == 'new_e2e_first_name'
    assert response['teacher_id'] == auth.teacher_id
    assert response['group_name'] == GROUP_NAME_2
    assert response['photo_link'] is None
    update_teacher_group_name_api(auth.token, MAIN_GROUP)


def test_add_child(auth):
    # add child api
    response = add_child_api(
        token=auth.token,
        first_name='test_first_name',
        last_name='test_last_name',
        parent1_phone_number='123',
        parent2_phone_number='456',
        group_name=MAIN_GROUP,
        gender='girl',
        birthday_date="2000 10 10")
    assert response['id_created'] is not None
    child_id = response['id_created']
    response = get_child_api(auth.token,
                             child_id=child_id)
    assert response['child_id'] == child_id
    assert response['last_name'] == 'test_last_name'
    assert response['first_name'] == 'test_first_name'
    assert response['parent1_phone_number'] == '123'
    assert response['parent2_phone_number'] == '456'
    assert response['group_name'] == MAIN_GROUP


def test_update_child_group_name(auth):
    response = add_child_api(
        token=auth.token,
        first_name='test_first_name',
        last_name='test_last_name',
        parent1_phone_number='123',
        parent2_phone_number='456',
        group_name=MAIN_GROUP,
        gender="boy",
        birthday_date="2000 10 10"
    )
    assert response['id_created'] is not None
    child_id = response['id_created']
    response = update_child_group_name_api(
        token=auth.token,
        child_id=child_id,
        group_name=GROUP_NAME_2)
    assert response['statusCode'] == '200'
    response = get_child_api(auth.token,
                             child_id=child_id)
    assert response['group_name'] == GROUP_NAME_2


def test_delete_child(auth):
    response = add_child_api(
        token=auth.token,
        first_name='test_first_name',
        last_name='test_last_name',
        parent1_phone_number='123',
        parent2_phone_number='456',
        group_name=MAIN_GROUP,
        gender='boy',
        birthday_date="2000 10 10")

    assert response['id_created'] is not None
    child_id = response['id_created']
    delete_child_api(token=auth.token, child_id=child_id)
    response = get_child_api(auth.token,
                             child_id=child_id)
    assert response == {
        'statusCode': '400',
        'message': 'Child not exist',
        'internal_code': '401'}


def test_kindergarten_exist(auth):
    response = get_teacher_api(auth.token)
    response = get_kindergarten_exist_api(response[KINDERGARTEN_ID])
    assert response


def test_get_kindergarten_info(auth):
    response = get_kindergarten_info_api(auth.token)
    assert response[KINDERGARTEN_NAME] == 'e2e_kindergarten_name'


def test_get_kindergarten_children(auth):
    response = get_kindergarten_children_api(auth.token)
    assert len(response) >= 2


def test_get_attendance_report(auth):
    response = get_attendance_report_api(token=auth.token, month="03")
    assert len(response) >= 2
