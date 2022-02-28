import random

from const import MAX_ID


def get_random_id() -> str:
    number = random.randint(1, MAX_ID)
    return str(number).zfill(8)
