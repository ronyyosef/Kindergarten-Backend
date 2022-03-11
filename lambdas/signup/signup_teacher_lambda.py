from shared.const import FIRST_NAME, LAST_NAME, KINDERGARTEN_ID, GROUP_NUMBER, IS_ADMIN, \
    KINDERGARTEN_NAME, TEACHER_ID
from shared.hanlders.KindergartenHandler import KindergartenHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator
from utils.random import get_random_id
from utils.logger import logger


@lambda_decorator
def signup_teacher(event, context):
    body: dict = event['customBody']

    if body.get(KINDERGARTEN_ID, None) is None:
        if KINDERGARTEN_NAME not in body:
            return "Error If kindergarten_id is null, new kindergarten_name must be provided"
        body[KINDERGARTEN_ID] = create_kindergarten_for_teacher(
            body[KINDERGARTEN_NAME])
    # TODO make sure kindergarten_id exist

    teacher_update_info = {
        TEACHER_ID: event[TEACHER_ID],
        FIRST_NAME: body.get(FIRST_NAME, None),
        LAST_NAME: body.get(LAST_NAME, None),
        KINDERGARTEN_ID: body.get(KINDERGARTEN_ID, None),
        GROUP_NUMBER: body.get(GROUP_NUMBER, None),
        IS_ADMIN: body.get(IS_ADMIN, None),
    }
    TeacherHandler.update_teacher(**teacher_update_info)


def create_kindergarten_for_teacher(kindergarten_name: str) -> str:
    id_is_in_use = True
    while id_is_in_use:
        id_for_added_kindergarten = get_random_id()
        id_is_in_use = KindergartenHandler.check_if_kindergarten_exists(
            id_for_added_kindergarten)
    logger.info(f"id to be used {id_for_added_kindergarten}")
    KindergartenHandler.add_kindergarten(
        id_for_added_kindergarten, kindergarten_name)
    return id_for_added_kindergarten
