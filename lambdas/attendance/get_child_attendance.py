from datetime import datetime

from shared.const import EVENT_QUERY_STRING
from shared.error_handling.error_codes import INPUT_ERROR
from shared.error_handling.exception import MyException
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.SpreadsheetHandler import SpreadsheetHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_child_attendance(event, context):
    child_id = event[EVENT_QUERY_STRING]["child_id"]
    child_exists = ChildrenHandler.check_if_key_exists(child_id)
    current_month = datetime.now().strftime('%m')
    month = event[EVENT_QUERY_STRING]["month"] if "month" in event[
        EVENT_QUERY_STRING] else current_month
    month = month.zfill(2)

    if child_exists:
        return SpreadsheetHandler.get_child_spreadsheet(
            child_id=child_id, month=month)
    raise MyException(f"Child {child_id} was not found ",INPUT_ERROR)
