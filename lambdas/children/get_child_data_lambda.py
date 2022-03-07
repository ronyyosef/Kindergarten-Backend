
from shared.ChildrenHandler import ChildrenHandler
from shared.lambda_decorator import lambda_decorator


@lambda_decorator
def get_child_data(event, context):
    response = ChildrenHandler.get_child(event["querystring"]["id"])
    return response
