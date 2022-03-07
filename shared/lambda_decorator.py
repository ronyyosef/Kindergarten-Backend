import json
import traceback

from shared.slack_notification import send_errors_alert_msg


def lambda_decorator(func):
    def inner(*args, **kwargs):
        try:
            lambda_result = func(*args, **kwargs)
            if lambda_result:
                return lambda_result
            else:
                return {"statusCode": "200"}
        except Exception as ex:
            tb = traceback.format_exc()
            send_errors_alert_msg(f'{str(ex)}: \n\n {str(tb)}')
    return inner


@lambda_decorator
def func(event, context):
    x = 4 / 0
    print("the func")


print(func({}, {}))
