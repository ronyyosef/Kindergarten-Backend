import datetime

from pydantic import BaseModel, Field, root_validator

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

    child_attendance = AttendanceHandler.get_attendance(child_id=data.child_id)
    attendance_exists = True if child_attendance is not None else False

    if attendance_exists:
        if data.is_present == "yes":
            AttendanceHandler.update_attendance(child_id=data.child_id, kindergarten_id=data.kindergarten_id,
                                                is_present="yes")
        elif data.is_present == "no":
            AttendanceHandler.delete_attendance(child_id=data.child_id)
        elif data.is_present == "notified_missing":
            AttendanceHandler.update_attendance(child_id=data.child_id, kindergarten_id=data.kindergarten_id,
                                                is_present="notified_missing")
    else:
        if data.is_present == "yes":
            AttendanceHandler.add_attendance(child_id=data.child_id, kindergarten_id=data.kindergarten_id,
                                             is_present="yes")
        elif data.is_present == "no":
            pass
        elif data.is_present == "notified_missing":
            AttendanceHandler.add_attendance(child_id=data.child_id, kindergarten_id=data.kindergarten_id,
                                             is_present="notified_missing")


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
        except KeyError:
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
