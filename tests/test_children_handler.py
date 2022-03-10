# from datetime import date

# from shared.AttendanceHandler import ChildrenHandler
from const import KINDERGARTEN_ID, FIRST_NAME, LAST_NAME, PHOTO_LINK, GROUP_NUMBER, PARENT1_PHONE_NUMBER, \
    PARENT2_PHONE_NUMBER, CHILD_ID

from shared.ChildrenHandler import ChildrenHandler


def setup_module():
    pass


def teardown_module():
    pass


def test_add_ChildHandler():
    ChildrenHandler.add_child(child_id='test_child_id',
                              kindergarten_id='test_kindergarten_id',
                              first_name='test_first_name',
                              last_name='test_last_name',
                              parent1_phone_number='test_parent1_phone_number',
                              parent2_phone_number='test_parent2_phone_number',
                              group_number='test_group_number',
                              )
    response = ChildrenHandler.get_child(child_id='test_child_id')
    assert response == {'child_id': 'test_child_id', 'last_name': 'test_last_name', 'group_number': 'test_group_number', 'kindergarten_id': 'test_kindergarten_id', 'first_name': 'test_first_name', 'parent2_phone_number': 'test_parent2_phone_number', 'parent1_phone_number': 'test_parent1_phone_number', 'photo_link': None}