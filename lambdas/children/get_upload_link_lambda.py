from shared.const import KINDERGARTEN_ID, TEACHER_ID
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.S3PhotosHandler import S3PhotosHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_upload_link(event, context):
    child_id = event['querystring']['child_id']
    try:
        child_data = ChildrenHandler.get_child(child_id)
    except:
        return 'child does not exist'
    child_kindergarten_id = child_data[KINDERGARTEN_ID]
    teacher_kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(event[TEACHER_ID])
    if child_kindergarten_id != teacher_kindergarten_id:
        return 'child and teacher does not in the same class'
    return S3PhotosHandler.put_photo_url(child_kindergarten_id, child_id)
