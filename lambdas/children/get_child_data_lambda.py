from shared.const import EVENT_QUERY_STRING
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_child_data(event, context):
    response = ChildrenHandler.get_child(event[EVENT_QUERY_STRING]["id"])
    child_id = response.get("child_id", None)
    if child_id:
        child_attendance = AttendanceHandler.get_attendance(child_id=child_id)
        if child_attendance:
            response["is_present"] = child_attendance.get("is_present", "no")
        else:
            response["is_present"] = "no"
    else:
        response = "Couldn't retrieve child"
    # TODO make sure this chile and his teacher from the same kindergarten
    return response
