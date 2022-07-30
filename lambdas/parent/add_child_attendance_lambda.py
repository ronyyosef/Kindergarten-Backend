# get parameter of date and child and update its attendance on spastic date
from shared.const import CHILD_ID, DATE, IS_PRESENT, KINDERGARTEN_ID, EVENT_BODY
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def add_child_attendance(event, context):
    return {
        DATE: event[EVENT_BODY][DATE],
        CHILD_ID: event[EVENT_BODY][CHILD_ID],
        IS_PRESENT: event[EVENT_BODY][IS_PRESENT],
        KINDERGARTEN_ID: event[EVENT_BODY][KINDERGARTEN_ID]}
    date = event[DATE]
    child_id = event[CHILD_ID]
    is_present = event[IS_PRESENT]
    kindergarten_id = event[KINDERGARTEN_ID]

    AttendanceHandler.add_attendance(
        date_query=date,
        child_id=child_id,
        is_present=is_present,
        kindergarten_id=kindergarten_id)
