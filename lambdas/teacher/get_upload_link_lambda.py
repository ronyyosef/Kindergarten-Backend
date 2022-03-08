from const import USER_ID
from shared.CognitoHandler import CognitoHandler
from shared.S3PhotosHandler import S3PhotosHandler
from shared.TeacherHandler import TeacherHandler
from shared.lambda_decorator import lambda_decorator


@lambda_decorator
def get_upload_link(event, context):
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(event[USER_ID])
    return S3PhotosHandler.put_photo_url(kindergarten_id, event[USER_ID])
