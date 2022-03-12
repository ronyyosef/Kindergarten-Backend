from datetime import date
from time import time

import boto3
from boto3.dynamodb.conditions import Key

from shared.const import ATTENDANCE_TABLE, ATTENDANCE_PK, ATTENDANCE_SK, \
    KINDERGARTEN_ID, TTL, \
    ATTENDANCE_TABLE_TTL_TIME_OUT, TIME_IN, TIME_OUT, CHILD_ID, DATE, IS_PRESENT

attendance_table = boto3.resource('dynamodb').Table(ATTENDANCE_TABLE)


class AttendanceHandler:

    @staticmethod
    def add_attendance(
            child_id: str,
            kindergarten_id: str,
            time_in: str = None,
            time_out: str = None,
            is_present: str = "no"):
        new_attendance = {
            ATTENDANCE_PK: child_id,
            ATTENDANCE_SK: str(date.today()),
            KINDERGARTEN_ID: kindergarten_id,
            TTL: int(time() + ATTENDANCE_TABLE_TTL_TIME_OUT),
            TIME_IN: time_in,
            TIME_OUT: time_out,
            IS_PRESENT: is_present
        }
        attendance_table.put_item(Item=new_attendance)
        return new_attendance

    @staticmethod
    def remove_attendance(child_id: str) -> None:
        attendance_table.delete_item(
            Key={ATTENDANCE_PK: child_id, ATTENDANCE_SK: str(date.today())})

    @staticmethod
    def get_attendance(child_id, date_query: str = str(date.today())):
        response = attendance_table.query(KeyConditionExpression=Key(
            ATTENDANCE_PK).eq(child_id) & Key(ATTENDANCE_SK).eq(date_query))
        attendance_data = response["Items"][0] if response[
                                                      'Count'] == 1 else None
        return attendance_data

    @staticmethod
    def get_attendance_for_entire_month(child_id, report_month):
        response = attendance_table.query(
            KeyConditionExpression=Key(ATTENDANCE_PK).eq(child_id) & Key(ATTENDANCE_SK).between(f"2022-{report_month}-00",f"2022-{report_month}-30"))
        attendance_data = response["Items"] if response['Count'] >= 1 else None
        return attendance_data

    @staticmethod
    def delete_attendance(child_id: str, date_query: str) -> None:
        response = attendance_table.delete_item(
            Key={
                ATTENDANCE_PK: child_id,
                ATTENDANCE_SK: date_query
            })
        return response

    @staticmethod
    def update_attendance(child_id: str,
                          date_query: str,
                          kindergarten_id: str,
                          time_in: str = None,
                          time_out: str = None,
                          is_present: str = "no") -> dict:
        response = attendance_table.update_item(
            Key={
                ATTENDANCE_PK: child_id,
                ATTENDANCE_SK: date_query},
            UpdateExpression=f'set {KINDERGARTEN_ID}=:1,'
                             f' {TIME_IN}=:2, {TIME_OUT}=:3, {IS_PRESENT} =:4',
            ExpressionAttributeValues={
                ':1': kindergarten_id,
                ':2': time_in,
                ':3': time_out,
                ':4': is_present,
            },
            ReturnValues='ALL_NEW')
        return response['Attributes']

    @staticmethod
    def check_if_attendance_exists(
            child_id: str, time_to_check: str = str(date.today())) -> bool:
        response = None
        try:
            response = attendance_table.query(
                KeyConditionExpression=Key(CHILD_ID).eq(
                    child_id) & Key(DATE).eq(time_to_check),
                Limit=1)
        except Exception as err:
            a = err
            print(err)

        return response['Count'] >= 1
