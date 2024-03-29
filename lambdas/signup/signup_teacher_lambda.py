from shared.const import FIRST_NAME, LAST_NAME, KINDERGARTEN_ID, GROUP_NAME, \
 \
    KINDERGARTEN_NAME, TEACHER_ID, MAIN_GROUP, EVENT_BODY
from shared.error_handling.error_codes import INPUT_ERROR
from shared.error_handling.exception import MyException
from shared.hanlders.GroupsHandler import GroupsHandler
from shared.hanlders.KindergartenHandler import KindergartenHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator
from utils.logger import logger
from utils.random import get_random_id


@lambda_decorator
def signup_teacher(event, context):
    body: dict = event[EVENT_BODY]

    if body.get(KINDERGARTEN_ID, None) is None:
        if KINDERGARTEN_NAME not in body:
            raise MyException(
                "Error If kindergarten_id is null, new kindergarten_name must be provided",
                INPUT_ERROR)
        body[KINDERGARTEN_ID] = create_kindergarten_for_teacher(
            body[KINDERGARTEN_NAME])
        GroupsHandler.add_group_to_kindergarten(
            body[KINDERGARTEN_ID], MAIN_GROUP)

    if KindergartenHandler.check_if_kindergarten_exists(
            body[KINDERGARTEN_ID]) is False:
        raise Exception(
            f"Kindergarten with id: {body[KINDERGARTEN_ID]} does not exist")

    teacher_update_info = {
        TEACHER_ID: event[TEACHER_ID],
        FIRST_NAME: body.get(FIRST_NAME, None),
        LAST_NAME: body.get(LAST_NAME, None),
        KINDERGARTEN_ID: body.get(KINDERGARTEN_ID, None),
        GROUP_NAME: MAIN_GROUP,
    }
    TeacherHandler.update_teacher(**teacher_update_info)


def create_kindergarten_for_teacher(kindergarten_name: str) -> str:
    id_is_in_use = True
    id_for_added_kindergarten = None
    while id_is_in_use:
        id_for_added_kindergarten = get_random_id()
        id_is_in_use = KindergartenHandler.check_if_kindergarten_exists(
            id_for_added_kindergarten)
    logger.info(f"id to be used {id_for_added_kindergarten}")
    KindergartenHandler.add_kindergarten(
        id_for_added_kindergarten, kindergarten_name)
    return id_for_added_kindergarten
