from datetime import date

from shared.hanlders.AttendanceHandler import AttendanceHandler
from shared.hanlders.ChildrenHandler import ChildrenHandler
from shared.hanlders.KindergartenHandler import KindergartenHandler
from shared.hanlders.SpreadsheetHandler import SpreadsheetHandler
from utils.random import get_random_id


def test_spreadsheet_handler():
    test_kindergarten_id = get_random_id()
    test_child_id = get_random_id()

    KindergartenHandler.add_kindergarten(test_kindergarten_id, 'test_name')
    ChildrenHandler.add_child(child_id=test_child_id,
                              kindergarten_id=test_kindergarten_id,
                              first_name='test_first_name',
                              last_name='test_last_name',
                              parent1_phone_number='test_parent1_phone_number',
                              parent2_phone_number='test_parent2_phone_number',
                              group_number='test_group_number',
                              )
    AttendanceHandler.add_attendance(
        child_id=test_child_id, kindergarten_id='test_kindergarten_id')

    spreadsheet_attendance = SpreadsheetHandler.get_kindergarten_spreadsheet(
        test_kindergarten_id)
    assert len(
        spreadsheet_attendance) == 1, "Report should have data of 1 child in it"
    KindergartenHandler.delete_kindergarten(
        kindergarten_id=test_kindergarten_id)
    ChildrenHandler.delete_child(child_id=test_child_id)
    AttendanceHandler.delete_attendance(child_id=test_child_id,
                                        date_query=str(date.today()))
