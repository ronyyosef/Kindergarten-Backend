
# return child_id and kindergarten id by  access token of parent
from shared.const import TEACHER_ID
from shared.hanlders.ParendHandler import ParentHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_parent_data(event, context):
    user_id = event[TEACHER_ID]
    return ParentHandler.get_parent_data(user_id)
