from shared.const import TEACHER_ID, CHILD_ID
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_kindergarten_children(event, context):
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(event[TEACHER_ID])
    children = ChildrenHandler.get_children_for_kindergarten(kindergarten_id)
    return children
