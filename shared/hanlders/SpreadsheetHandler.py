from datetime import datetime

from shared.const import MARCH
from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.KindergartenHandler import KindergartenHandler
import pandas as pd


class SpreadsheetHandler:

    @staticmethod
    def get_kindergarten_spreadsheet(kindergarten_id: str, month=MARCH):
        kindergarten_data = KindergartenHandler.get_kindergarten(kindergarten_id)
        kindergarten_id = kindergarten_data["kindergarten_id"]

        columns = ["child_name", "day", "time_in", "time_out", "total_stay", "ate_pizza"]
        children = ChildrenHandler.get_children_for_kindergarten(kindergarten_id, )
        df_children_list = []
        for child in children:
            child["monthly_attendance_report"] = AttendanceHandler.get_attendance_for_entire_month(child["child_id"],
                                                                                                   month)
            if child["monthly_attendance_report"] is None:
                child["monthly_attendance_report"] = []

            df_child = pd.DataFrame(child, columns=columns)

            time_in_list = [attendance["time_in"] for attendance in child["monthly_attendance_report"]]
            time_out_list = [attendance["time_out"] for attendance in child["monthly_attendance_report"]]
            total_stay = []

            for time_in, time_out in zip(time_in_list, time_out_list):
                stay_to_append = ""
                if time_in and time_out:
                    time_in_obj = datetime.strptime(time_in, "%H:%M:%S")
                    time_out_obj = datetime.strptime(time_out, "%H:%M:%S")
                    if time_out_obj > time_in_obj:
                        stay_to_append = str(time_out_obj - time_in_obj)
                total_stay.append(stay_to_append)
            ate_pizza = []
            day = [attendance["date"] for attendance in child["monthly_attendance_report"]]
            df_child["time_in"] = pd.Series(time_in_list, dtype=pd.StringDtype())
            df_child["day"] = pd.Series(day, dtype=pd.StringDtype())
            df_child["time_out"] = pd.Series(time_out_list, dtype=pd.StringDtype())
            df_child["total_stay"] = pd.Series(total_stay, dtype=pd.StringDtype())
            df_child["ate_pizza"] = pd.Series(ate_pizza, dtype=pd.StringDtype())
            df_child["child_name"] = f'{child["first_name"]} {child["last_name"]}'
            df_child = df_child.fillna("")
            df_children_list.append(df_child.to_csv())

        return df_children_list
