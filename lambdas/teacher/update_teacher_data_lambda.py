from const import PHONE_NUMBER, FIRST_NAME, LAST_NAME, PHOTO_LINK, KINDERGARTEN_ID, GROUP_NUMBER, IS_ADMIN
from shared.CognitoHandler import CognitoHandler
from shared.TeacherHandler import TeacherHandler


def update_teacher_data(event, context):
    teacher_id = CognitoHandler.get_user_id(event)
    body: dict = event['customBody']
    teacher_update_info = {
        PHONE_NUMBER: teacher_id,
        FIRST_NAME: body.get(FIRST_NAME, None),
        LAST_NAME: body.get(LAST_NAME, None),
        PHOTO_LINK: body.get(PHOTO_LINK, None),
        KINDERGARTEN_ID: body.get(KINDERGARTEN_ID, None),
        GROUP_NUMBER: body.get(GROUP_NUMBER, None),
        IS_ADMIN: body.get(IS_ADMIN, None),
    }
    response = TeacherHandler.update_teacher(**teacher_update_info)
    return response
