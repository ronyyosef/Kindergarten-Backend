from const import TEACHER_ID
from shared.KindergartenHandler import KindergartenHandler
from shared.TeacherHandler import TeacherHandler
from shared.lambda_decorator import lambda_decorator


@lambda_decorator
def get_kindergarten_data(event, context):
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(event[TEACHER_ID])
    kindergarten_data = KindergartenHandler.get_kindergarten(kindergarten_id)
    return kindergarten_data