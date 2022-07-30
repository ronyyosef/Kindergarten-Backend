# get parameter of date and child and update its attendance on spastic date
from shared.const import CHILD_ID, DATE, IS_PRESENT, KINDERGARTEN_ID
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def add_child_attendance(event, context):
    date = event[DATE]
    child_id = event[CHILD_ID]
    is_present = event[IS_PRESENT]
    kindergarten_id = event[KINDERGARTEN_ID]

    AttendanceHandler.add_attendance(
        date_query=date,
        child_id=child_id,
        is_present=is_present,
        kindergarten_id=kindergarten_id)
