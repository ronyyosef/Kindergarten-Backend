from shared.ChildrenHandler import ChildrenHandler
from shared.CognitoHandler import CognitoHandler
from shared.S3PhotosHandler import S3PhotosHandler
from shared.TeacherHandler import TeacherHandler


def get_upload_link(event, context):
    item_id = event['querystring']['child_id']
    if not ChildrenHandler.check_if_key_exists(item_id):
        return 'child id not exist'

    user = CognitoHandler.get_user_id(event)
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(user)
    return S3PhotosHandler.put_photo_url(kindergarten_id, user)
