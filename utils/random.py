import random

from const import MAX_ID
from logger import logger


def get_random_id() -> str:
    number = random.randint(1, MAX_ID)
    logger.info(f"id generated {id}")
    return str(number).zfill(8)
