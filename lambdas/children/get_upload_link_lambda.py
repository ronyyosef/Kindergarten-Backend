from shared.const import KINDERGARTEN_ID, TEACHER_ID, EVENT_QUERY_STRING
from shared.error_handling.error_codes import INPUT_ERROR
from shared.error_handling.exception import MyException
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.ParendHandler import ParentHandler
from shared.hanlders.S3PhotosHandler import S3PhotosHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_upload_link(event, context):
    parent_data = ParentHandler.get_parent_data(event[TEACHER_ID]).get('Item')
    if parent_data is not None:
        child_id = parent_data['child_id']
        child_kindergarten_id = parent_data['kindergarten_id']
    else:
        child_id = event[EVENT_QUERY_STRING]['child_id']
        try:
            child_data = ChildrenHandler.get_child(child_id)
        except BaseException:
            raise MyException('child does not exist', INPUT_ERROR)
        child_kindergarten_id = child_data[KINDERGARTEN_ID]
        teacher_kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(
            event[TEACHER_ID])
        if child_kindergarten_id != teacher_kindergarten_id:
            return MyException(
                'child and teacher does not in the same class',
                INPUT_ERROR)
    return S3PhotosHandler.put_photo_url(child_kindergarten_id, child_id)
