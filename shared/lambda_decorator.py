import traceback

from const import TEACHER_ID
from shared.CognitoHandler import CognitoHandler
from shared.slack_notification import send_errors_alert_msg


def lambda_decorator(lambda_function):
    def inner(*args, **kwargs):
        try:
            event = args[0]
            context = args[1]
            event[TEACHER_ID] = CognitoHandler.get_teacher_id(event)
            lambda_result = lambda_function(event, event)
            if lambda_result is not None:
                return lambda_result
            else:
                return {"statusCode": "200"}
        except Exception as ex:
            tb = traceback.format_exc()
            send_errors_alert_msg(f'{str(ex)}: \n\n {str(tb)}')
            return {"statusCode": "500",
                    "message": "internal server error"}

    return inner