from const import KINDERGARTEN_ID, USER_ID
from shared.CognitoHandler import CognitoHandler
from shared.KindergartenHandler import KindergartenHandler
from shared.TeacherHandler import TeacherHandler
from shared.lambda_decorator import lambda_decorator


@lambda_decorator
def get_kindergarten_data(event, context):
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(event[USER_ID])
    kindergarten_data = KindergartenHandler.get_kindergarten(kindergarten_id)
    return kindergarten_data