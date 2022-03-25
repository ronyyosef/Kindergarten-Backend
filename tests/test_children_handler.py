import os

from shared.hanlders.ChildrenHandler import ChildrenHandler
from utils.random import get_random_id


def setup_module():
    pass


def teardown_module():
    pass


def test_add_child_handler():
    ChildrenHandler.add_child(child_id='test_child_id',
                              kindergarten_id='test_kindergarten_id',
                              first_name='test_first_name',
                              last_name='test_last_name',
                              parent1_phone_number='test_parent1_phone_number',
                              parent2_phone_number='test_parent2_phone_number',
                              group_number='test_group_number',
                              )
    response = ChildrenHandler.get_child(child_id='test_child_id')
    assert response == {
        'child_id': 'test_child_id',
        'last_name': 'test_last_name',
        'group_number': 'test_group_number',
        'kindergarten_id': 'test_kindergarten_id',
        'first_name': 'test_first_name',
        'parent2_phone_number': 'test_parent2_phone_number',
        'parent1_phone_number': 'test_parent1_phone_number',
        'photo_link': None}


def test_delete_child_handler():
    test_child_id = get_random_id()
    ChildrenHandler.add_child(child_id=test_child_id,
                              kindergarten_id='test_kindergarten_id',
                              first_name='test_first_name',
                              last_name='test_last_name',
                              parent1_phone_number='test_parent1_phone_number',
                              parent2_phone_number='test_parent2_phone_number',
                              group_number='test_group_number',
                              )
    response = ChildrenHandler.get_child(child_id=test_child_id)
    assert response == {
        'child_id': test_child_id,
        'last_name': 'test_last_name',
        'group_number': 'test_group_number',
        'kindergarten_id': 'test_kindergarten_id',
        'first_name': 'test_first_name',
        'parent2_phone_number': 'test_parent2_phone_number',
        'parent1_phone_number': 'test_parent1_phone_number',
        'photo_link': None}

    ChildrenHandler.delete_child(child_id=test_child_id,
                                 kindergarten_id=response["kindergarten_id"])
    response = ChildrenHandler.get_child(child_id=test_child_id)
    assert response is None
