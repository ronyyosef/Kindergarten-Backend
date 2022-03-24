from shared.hanlders.GroupsHandler import GroupsHandler
from utils.random import get_random_id

test_kindergarten_id = "f5bb3f4b"


def test_add_groups():
    random_id = get_random_id()
    GroupsHandler.add_group_to_kindergarten(test_kindergarten_id, random_id)
    response = GroupsHandler.get_kindergarten_groups(test_kindergarten_id)
    assert random_id in response["groups_in_kindergarten"], f"Group with name {random_id} failed to create"


def test_get_groups():
    response = GroupsHandler.get_kindergarten_groups(test_kindergarten_id)
    assert "תינוקייה" in response["groups_in_kindergarten"]


def test_delete_groups():
    random_id = get_random_id()
    GroupsHandler.add_group_to_kindergarten(test_kindergarten_id, random_id)
    response = GroupsHandler.get_kindergarten_groups(test_kindergarten_id)
    assert random_id in response["groups_in_kindergarten"], f"Group with name {random_id} failed to create"
    GroupsHandler.delete_group_from_kindergarten(test_kindergarten_id, random_id)
    response = GroupsHandler.get_kindergarten_groups(test_kindergarten_id)
    assert random_id not in response["groups_in_kindergarten"], f"Group with name {random_id} failed to delete"
