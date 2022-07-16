from shared.const import TEACHER_ID, EVENT_QUERY_STRING
from shared.hanlders.SpreadsheetHandler import SpreadsheetHandler
from shared.hanlders.TeacherHandler import TeacherHandler
from shared.hanlders.lambda_decorator import lambda_decorator
from datetime import datetime
from shared.const import MARCH, MAY, IS_PRESENT
from datetime import date

@lambda_decorator
def get_attendance_spreadsheet(event, context):
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(event[TEACHER_ID])

    current_month = datetime.now().strftime('%m')
    month = event[EVENT_QUERY_STRING]["month"] if "month" in event[
        EVENT_QUERY_STRING] else current_month
    month = month.zfill(2)
    attendance_report_data = SpreadsheetHandler.get_kindergarten_spreadsheet(kindergarten_id=kindergarten_id,
                                                                             month=month)
    return attendance_report_data
