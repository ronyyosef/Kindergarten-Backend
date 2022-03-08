import uuid


def get_random_id() -> str:
    return str(uuid.uuid1())[:8]
