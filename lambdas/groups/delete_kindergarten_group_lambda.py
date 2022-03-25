from shared.const import TEACHER_ID, EVENT_BODY
from shared.hanlders.GroupsHandler import GroupsHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def delete_kindergarten_group(event, context):
    teacher_data = TeacherHandler.get_teacher_data(event[TEACHER_ID])
    kindergarten_id = teacher_data.get("kindergarten_id")
    body: dict = event[EVENT_BODY]
    group_name_to_delete = body["group_name"]
    GroupsHandler.delete_group_from_kindergarten(kindergarten_id, group_name_to_delete)
