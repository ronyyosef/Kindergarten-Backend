from shared.const import TEACHER_ID, EVENT_BODY, GROUP_NAME, KINDERGARTEN_ID, \
    MAIN_GROUP
from shared.error_handling.error_codes import INPUT_ERROR
from shared.error_handling.exception import MyException
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.GroupsHandler import GroupsHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


def group_is_empty(teacher_data: dict) -> bool:
    children = ChildrenHandler.get_children_for_kindergarten_and_group_no_photo_link(
        kindergarten_id=teacher_data.get(KINDERGARTEN_ID),
        group_name=teacher_data.get(GROUP_NAME))
    teachers = TeacherHandler.get_all_teacher_in_group(teacher_data)
    return bool(len(children) == 0) and bool(len(teachers) == 0)


@lambda_decorator
def delete_kindergarten_group(event, context):
    teacher_data = TeacherHandler.get_teacher_data(event[TEACHER_ID])
    kindergarten_id = teacher_data.get("kindergarten_id")
    body: dict = event[EVENT_BODY]
    group_name_to_delete = body["group_name"]
    if group_name_to_delete == MAIN_GROUP:
        raise MyException("the main group cannot be deleted", INPUT_ERROR)
    if group_is_empty(teacher_data, group_name_to_delete) is True:
        GroupsHandler.delete_group_from_kindergarten(kindergarten_id,
                                                     group_name_to_delete)
    else:
        raise MyException(
            "there are children or teachers in that group, move them to "
            "another group "
            "and then try to delete again",
            INPUT_ERROR)
