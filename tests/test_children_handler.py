# from datetime import date

# from shared.AttendanceHandler import ChildrenHandler
from const import ID, KINDERGARTEN_ID, FIRST_NAME, LAST_NAME, PHOTO_LINK, GROUP_NUMBER, PARENT1_PHONE_NUMBER, \
    PARENT2_PHONE_NUMBER

from shared.ChildrenHandler import ChildrenHandler


def setup_module():
    pass


def teardown_module():
    pass


def test_add_ChildHandler():
    response = ChildrenHandler.add_child(id='test_child_id',
                                         kindergarten_id='test_kindergarten_id',
                                         first_name='test_first_name',
                                         last_name='test_last_name',
                                         parent1_phone_number='test_parent1_phone_number',
                                         parent2_phone_number='test_parent2_phone_number',
                                         group_number='test_group_number',
                                         )

    assert response['ResponseMetadata']['HTTPStatusCode'] == 200


def test_get_ChildHandler():
    response = ChildrenHandler.get_child(id='test_child_id')
    assert response == {ID: 'test_child_id',
                        KINDERGARTEN_ID: 'test_kindergarten_id',
                        FIRST_NAME: 'test_first_name',
                        LAST_NAME: 'test_last_name',
                        PARENT1_PHONE_NUMBER: 'test_parent1_phone_number',
                        PARENT2_PHONE_NUMBER: 'test_parent2_phone_number',
                        GROUP_NUMBER: 'test_group_number'}
