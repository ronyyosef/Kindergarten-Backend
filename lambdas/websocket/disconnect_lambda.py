import logging

from shared.hanlders.lambda_decorator import lambda_decorator


#@lambda_decorator
from utils.logger import logger


def disconnect(event, context):
    logger.info(event)
    return {"statusCode": 200, "body": 'some body'}
