from datetime import datetime

from shared.const import MARCH
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.KindergartenHandler import KindergartenHandler


class SpreadsheetHandler:

    @staticmethod
    def get_kindergarten_spreadsheet(kindergarten_id: str, month=MARCH):
        kindergarten_data = KindergartenHandler.get_kindergarten(kindergarten_id)
        kindergarten_id = kindergarten_data["kindergarten_id"]

        children = ChildrenHandler.get_children_for_kindergarten(kindergarten_id, )
        report_generated = {}
        for child in children:
            child_name = f'{child["first_name"]} {child["last_name"]}'
            child_id = child["child_id"]
            report_generated[child_id] = "child_name, day, time_in, time_out, total_stay, ate_pizza\n"
            child["monthly_attendance_report"] = AttendanceHandler.get_attendance_for_entire_month(child["child_id"],
                                                                                                   month)

            if child["monthly_attendance_report"] is None:
                child["monthly_attendance_report"] = []
            for attendance in child["monthly_attendance_report"]:
                time_in = attendance.get("time_in", None)
                time_out = attendance.get("time_out", None)
                total_stay = ""
                ate_pizza = ""
                day = attendance.get("date", None)

                if time_in and time_out:
                    time_in_obj = datetime.strptime(time_in, "%H:%M:%S")
                    time_out_obj = datetime.strptime(time_out, "%H:%M:%S")
                    if time_out_obj > time_in_obj:
                        total_stay = str(time_out_obj - time_in_obj)
                else:
                    time_in = time_out = ""

                report_generated[child_id] += (','.join(
                    [child_name, day, time_in, time_out, total_stay,
                     ate_pizza])) + "\n"

        return report_generated

    @staticmethod
    def get_child_spreadsheet(child_id: str, month=MARCH):
        child = ChildrenHandler.get_child(child_id)
        report_generated = {}
        report_generated["notified_missing"] = []
        report_generated["arrived"] = []
        monthly_attendance_report = AttendanceHandler.get_attendance_for_entire_month(child["child_id"], month)
        if monthly_attendance_report:
            for attendance in monthly_attendance_report:
                if attendance["is_present"] == "notified_missing":
                    report_generated["notified_missing"].append(attendance["date"])
                if attendance["is_present"] == "yes" or attendance["is_present"] == "no":
                    report_generated["arrived"].append(attendance["date"])

        report_generated["notified_missing"] = sorted(report_generated["notified_missing"])
        report_generated["arrived"] = sorted(report_generated["arrived"])
        return report_generated
