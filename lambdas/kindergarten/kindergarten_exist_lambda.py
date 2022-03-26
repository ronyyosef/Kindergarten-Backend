from shared.const import KINDERGARTEN_ID
from shared.error_handling.error_codes import INPUT_ERROR
from shared.error_handling.exception import MyException
from shared.hanlders.KindergartenHandler import KindergartenHandler


def kindergarten_exist(event, context):
    data = event.get("querystring")
    kindergarten_id = data.get(KINDERGARTEN_ID, None)
    if kindergarten_id is not None:
        if len(kindergarten_id) != 8:
            return False
        return KindergartenHandler.check_if_kindergarten_exists(
            kindergarten_id)
    else:
        return {"statusCode": "400",
                "message": "kindergarten_id is missing",
                "internal_code": INPUT_ERROR}
