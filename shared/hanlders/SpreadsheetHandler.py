from datetime import datetime

from shared.const import MARCH, MAY, IS_PRESENT
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.KindergartenHandler import KindergartenHandler
from datetime import date

class SpreadsheetHandler:

    @staticmethod
    def get_kindergarten_spreadsheet(kindergarten_id: str, month=MARCH):
        kindergarten_data = KindergartenHandler.get_kindergarten(kindergarten_id)
        kindergarten_id = kindergarten_data["kindergarten_id"]

        children = ChildrenHandler.get_children_for_kindergarten(kindergarten_id)
        report_generated = []
        report_generated.append(["דוח נוכחות"])
        list_of_days_index = list(range(1, 31 + 1))
        list_of_days_index.insert(0,'') # blank cell for alignment
        report_generated.append(list_of_days_index )# Creating days column names
        
        for child in children:
            child_name = f'{child["first_name"]} {child["last_name"]}'
            child_id = child["child_id"]

            monthly_attendance_report = AttendanceHandler.get_attendance_for_entire_month(child_id, month)
            child_addndance_vector = []
            for i in range(31):
                child_addndance_vector.append('-')

            if monthly_attendance_report:
                for attendance in monthly_attendance_report:
                    if attendance[IS_PRESENT] == "yes":
                        child_addndance_vector[int(attendance["date"].split("-")[-1])-1] = 'YES'

            child_addndance_vector.insert(0, child_name)
            report_generated.append(child_addndance_vector)
        return report_generated

    @staticmethod
    def get_child_spreadsheet(child_id: str, month):
        child = ChildrenHandler.get_child(child_id)
        report_generated = {}
        report_generated["notified_missing"] = []
        report_generated["arrived"] = []
        monthly_attendance_report = AttendanceHandler.get_attendance_for_entire_month(child["child_id"], month)
        if monthly_attendance_report:
            for attendance in monthly_attendance_report:
                if attendance[IS_PRESENT] == "notified_missing":
                    report_generated["notified_missing"].append(attendance["date"])
                if attendance[IS_PRESENT] == "yes":
                    report_generated["arrived"].append(attendance["date"])

        report_generated["notified_missing"] = sorted(report_generated["notified_missing"])
        report_generated["arrived"] = sorted(report_generated["arrived"])
        return report_generated

#SpreadsheetHandler.get_kindergarten_spreadsheet('238595d7','06')