import logging

from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def disconnect(event, context):
    logging.log(event)
    return {"statusCode": 200, "body": 'some body'}
