from shared.const import EVENT_QUERY_STRING
from shared.error_handling.error_codes import INPUT_ERROR
from shared.error_handling.exception import MyException
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_child_data(event, context):
    response = ChildrenHandler.get_child(event[EVENT_QUERY_STRING]["id"])
    if response is None:
        MyException("Child not exist", INPUT_ERROR)
    child_id = response.get("child_id", None)
    if child_id:
        child_attendance = AttendanceHandler.get_attendance(child_id=child_id)
        if child_attendance:
            response["is_present"] = child_attendance.get("is_present", "no")
        else:
            response["is_present"] = "no"
    else:
        response = "Couldn't retrieve child"
    return response
