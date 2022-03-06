from const import KINDERGARTEN_ID
from shared.ChildrenHandler import ChildrenHandler
from shared.CognitoHandler import CognitoHandler
from shared.S3PhotosHandler import S3PhotosHandler
from shared.TeacherHandler import TeacherHandler


def get_upload_link(event, context):
    child_id = event['querystring']['child_id']
    try:
        child_data = ChildrenHandler.get_child(child_id)
    except:
        return 'child does not exist'
    child_kindergarten_id = child_data[KINDERGARTEN_ID]
    user = CognitoHandler.get_user_id(event)
    teacher_kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(user)
    if child_kindergarten_id != teacher_kindergarten_id:
        return 'child and teacher does not in the same class'
    return S3PhotosHandler.put_photo_url(child_kindergarten_id, child_id)
