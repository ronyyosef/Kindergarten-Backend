from const import KINDERGARTEN_ID
from shared.CognitoHandler import CognitoHandler
from shared.KindergartenHandler import KindergartenHandler
from shared.TeacherHandler import TeacherHandler


def get_kindergarten_data(event, context):
    user = CognitoHandler.get_user_id(event)
    teacher_data = TeacherHandler.get_teacher_data(user)
    kindergarten_id = teacher_data.get(KINDERGARTEN_ID)
    kindergarten_data = KindergartenHandler.get_kindergarten(kindergarten_id)
    return kindergarten_data