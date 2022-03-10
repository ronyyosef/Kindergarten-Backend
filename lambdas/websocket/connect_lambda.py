import logging

from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def connect(event, context):
    logging.info(event)
    return {"statusCode": 200, "body": 'some body'}