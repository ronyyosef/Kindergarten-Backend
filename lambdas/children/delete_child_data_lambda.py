from shared.const import TEACHER_ID, EVENT_BODY
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator
from utils.logger import logger


@lambda_decorator
def delete_child_data(event, context):
    teacher_data = TeacherHandler.get_teacher_data(event[TEACHER_ID])
    body: dict = event[EVENT_BODY]
    child_id_to_delete = body.get("id")
    child = ChildrenHandler.get_child(child_id_to_delete)
    if child["kindergarten_id"] != teacher_data["kindergarten_id"]:
        raise Exception(
            f'child id {child_id_to_delete} cant be deleted by teacher in kindergarten{teacher_data["kindergarten_id"]}')

    if child:
        ChildrenHandler.delete_child(child_id_to_delete, child["kindergarten_id"])
