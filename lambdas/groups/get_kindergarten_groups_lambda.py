from shared.const import TEACHER_ID
from shared.hanlders.GroupsHandler import GroupsHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_kindergarten_groups(event, context):
    teacher_data = TeacherHandler.get_teacher_data(event[TEACHER_ID])
    kindergarten_id = teacher_data.get("kindergarten_id")
    groups_in_kindergarten = GroupsHandler.get_kindergarten_groups(kindergarten_id)
    return groups_in_kindergarten
