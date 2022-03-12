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

        columns = ["child_name", "day", "time_in", "time_out", "total_stay", "ate_pizza"]
        children = ChildrenHandler.get_children_for_kindergarten(kindergarten_id, )
        report_generated = {}
        for child in children:
            child_name = f'{child["first_name"]} {child["last_name"]}'
            report_generated[child_name] = ""

            child["monthly_attendance_report_csv"] = []
            child["monthly_attendance_report"] = AttendanceHandler.get_attendance_for_entire_month(child["child_id"],
                                                                                                   month)

            if child["monthly_attendance_report"] is None:
                child["monthly_attendance_report"] = []
            for attendance in child["monthly_attendance_report"]:
                time_in = ""
                time_out = ""
                total_stay = ""
                ate_pizza = ""
                day = ""
                time_in_obj_data = attendance["time_in"]
                time_out_obj_data = attendance["time_out"]
                if time_in_obj_data and time_out_obj_data:
                    time_in_obj = datetime.strptime(time_in_obj_data, "%H:%M:%S")
                    time_out_obj = datetime.strptime(time_out_obj_data, "%H:%M:%S")
                    if time_out_obj > time_in_obj:
                        total_stay = str(time_out_obj - time_in_obj)
                day = attendance.get("date", "")

                report_generated[child_name] += (','.join(
                    [child_name, day, time_in, time_out, total_stay, ate_pizza])) + "\n"

                # df_children_list.append(df_child.to_csv())

        return report_generated
