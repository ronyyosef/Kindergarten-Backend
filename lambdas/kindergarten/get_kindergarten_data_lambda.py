from const import KINDERGARTEN_ID
from shared.CognitoHandler import CognitoHandler
from shared.KindergartenHandler import KindergartenHandler
from shared.TeacherHandler import TeacherHandler


def get_kindergarten_data(event, context):
    user = CognitoHandler.get_user_id(event)
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(user)
    kindergarten_data = KindergartenHandler.get_kindergarten(kindergarten_id)
    return kindergarten_data