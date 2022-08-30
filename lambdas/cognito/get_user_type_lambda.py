from shared.const import TEACHER_ID
from shared.hanlders.ParentHandler import ParentHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_user_type(event, context):
    user_id = event[TEACHER_ID]
    if ParentHandler.get_parent_data(user_id).get('Item') is None:
        return 'teacher'
    else:
        return 'parent'
