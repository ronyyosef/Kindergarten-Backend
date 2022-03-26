from shared.hanlders.GroupsHandler import GroupsHandler
from utils.random import get_random_id

test_kindergarten_id = "6cbe4a65"
test_group_name = "test_group_name"


def test_add_groups():
    test_group_name = "test_group_name"
    GroupsHandler.add_group_to_kindergarten(
        kindergarten_id=test_kindergarten_id,
        group_name=test_group_name)
    response = GroupsHandler.get_kindergarten_groups(test_kindergarten_id)
    assert test_group_name in response[
        "groups_in_kindergarten"], f"Group with name {test_group_name} failed to create"


def test_get_groups():
    response = GroupsHandler.get_kindergarten_groups(test_kindergarten_id)
    assert test_group_name in response["groups_in_kindergarten"]


def test_delete_groups():
    random_id = get_random_id()
    GroupsHandler.add_group_to_kindergarten(test_kindergarten_id, random_id)
    response = GroupsHandler.get_kindergarten_groups(test_kindergarten_id)
    assert random_id in response[
        "groups_in_kindergarten"], f"Group with name {random_id} failed to create"
    GroupsHandler.delete_group_from_kindergarten(
        test_kindergarten_id, random_id)
    response = GroupsHandler.get_kindergarten_groups(test_kindergarten_id)
    assert random_id not in response[
        "groups_in_kindergarten"], f"Group with name {random_id} failed to delete"
