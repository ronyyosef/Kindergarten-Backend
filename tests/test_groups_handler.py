import pytest

from shared.hanlders.GroupsHandler import GroupsHandler
from utils.random import get_random_id

TEST_KINDERGARTEN_ID = "6cbe4a65"
TEST_GROUP_NAME = "test_group_name"


@pytest.mark.skip()
def test_add_groups():
    test_group_name = "test_group_name"
    GroupsHandler.add_group_to_kindergarten(
        kindergarten_id=TEST_KINDERGARTEN_ID,
        group_name=test_group_name)
    response = GroupsHandler.get_kindergarten_groups(TEST_KINDERGARTEN_ID)
    assert test_group_name in response[
        "groups_in_kindergarten"], f"Group with name {test_group_name} failed to create"


@pytest.mark.skip()
def test_get_groups():
    response = GroupsHandler.get_kindergarten_groups(TEST_KINDERGARTEN_ID)
    assert TEST_GROUP_NAME in response["groups_in_kindergarten"]


@pytest.mark.skip()
def test_delete_groups():
    random_id = get_random_id()
    GroupsHandler.add_group_to_kindergarten(TEST_KINDERGARTEN_ID, random_id)
    response = GroupsHandler.get_kindergarten_groups(TEST_KINDERGARTEN_ID)
    assert random_id in response[
        "groups_in_kindergarten"], f"Group with name {random_id} failed to create"
    GroupsHandler.delete_group_from_kindergarten(
        TEST_KINDERGARTEN_ID, random_id)
    response = GroupsHandler.get_kindergarten_groups(TEST_KINDERGARTEN_ID)
    assert random_id not in response[
        "groups_in_kindergarten"], f"Group with name {random_id} failed to delete"
