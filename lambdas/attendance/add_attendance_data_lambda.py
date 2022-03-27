import datetime

from pydantic import BaseModel, Field, root_validator, validator

from shared.const import TEACHER_ID, CHILD_ID, DATE, KINDERGARTEN_ID, TIME_OUT, \
    TIME_IN, IS_PRESENT, EVENT_BODY, ID
from shared.error_handling.error_codes import INPUT_ERROR
from shared.error_handling.exception import MyException
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def add_attendance_data(event, context):
    data = InputData(**event)

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    child_attendance = AttendanceHandler.get_attendance(child_id=data.child_id)
    if AttendanceHandler.get_attendance(child_id=data.child_id) is None:
        child_attendance = AttendanceHandler.add_attendance(
            child_id=data.child_id, kindergarten_id=data.kindergarten_id)

    if data.is_present == "yes":
        child_attendance["time_in"] = current_time
        child_attendance["is_present"] = "yes"
        child_attendance["time_out"] = None
    elif data.is_present == "no":
        child_attendance["time_out"] = current_time
        child_attendance["is_present"] = "no"
    elif data.is_present == "notified_missing":
        child_attendance["is_present"] = "notified_missing"
        child_attendance["time_in"] = None
        child_attendance["time_out"] = None

    AttendanceHandler.update_attendance(
        child_id=child_attendance.get(
            CHILD_ID, None), date_query=child_attendance.get(
            DATE, None), kindergarten_id=child_attendance.get(
            KINDERGARTEN_ID, None), time_out=child_attendance.get(
            TIME_OUT, None), time_in=child_attendance.get(
            TIME_IN, None), is_present=child_attendance.get(
            IS_PRESENT, None))


class InputData(BaseModel):
    child_id: str = Field(..., alies=CHILD_ID)
    is_present: str = Field(..., alias=IS_PRESENT)
    teacher_id: str = Field(..., alias=TEACHER_ID)
    kindergarten_id: str = Field(..., alias=KINDERGARTEN_ID)

    @root_validator(pre=True)
    @classmethod
    def validate_data(cls, values):
        try:
            values[CHILD_ID] = values[EVENT_BODY][ID]
            values[IS_PRESENT] = values[EVENT_BODY][IS_PRESENT]
        except BaseException:
            raise MyException("Input Error", INPUT_ERROR)

        if values[IS_PRESENT] != 'yes' and values[IS_PRESENT] != 'no':
            raise MyException("is_present should be: yes|no", INPUT_ERROR)

        values[
            KINDERGARTEN_ID] = TeacherHandler.get_teacher_kindergarten_id(
            values[TEACHER_ID])

        if not ChildrenHandler.child_in_kindergarten(
                values[CHILD_ID], values[KINDERGARTEN_ID]):
            raise MyException(
                'child not exist/ child not in this kindergarten',
                INPUT_ERROR)

        return values
