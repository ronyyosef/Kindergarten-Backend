import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def add_teacher_data(event, context):
    logger.info("Adding new teacher")
    logger.info(f'event : {event}')
    return
