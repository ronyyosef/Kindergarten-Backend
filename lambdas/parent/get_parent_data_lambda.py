# return child_id and kindergarten id by  access token of parent
from shared.const import TEACHER_ID, KINDERGARTEN_ID, CHILD_ID, PHOTO_LINK
from shared.hanlders.ParentHandler import ParentHandler


from shared.hanlders.S3PhotosHandler import S3PhotosHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_parent_data(event, context):
    user_id = event[TEACHER_ID]
    parent_data = ParentHandler.get_parent_data(user_id)['Item']
    photo_link = S3PhotosHandler.get_photo_url(
        kindergarten_id=parent_data[KINDERGARTEN_ID],
        id=parent_data[CHILD_ID])
    parent_data[PHOTO_LINK] = photo_link
    return parent_data
