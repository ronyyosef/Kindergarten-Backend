from shared.const import TEACHER_ID, EVENT_QUERY_STRING
from shared.hanlders.SpreadsheetHandler import SpreadsheetHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator


@lambda_decorator
def get_attendance_spreadsheet(event, context):
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(event[TEACHER_ID])
    attendance_report_data = SpreadsheetHandler.get_kindergarten_spreadsheet(kindergarten_id=kindergarten_id,
                                                                             month=event[EVENT_QUERY_STRING]['month'])
    return attendance_report_data
