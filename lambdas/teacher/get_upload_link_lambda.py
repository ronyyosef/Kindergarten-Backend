from shared.const import TEACHER_ID
from shared.hanlders.S3PhotosHandler import S3PhotosHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_upload_link(event, context):
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(
        event[TEACHER_ID])
    return S3PhotosHandler.put_photo_url(kindergarten_id, event[TEACHER_ID])
