import csv
import logging
import os
from shared.hanlders.lambda_decorator import lambda_decorator
from datetime import datetime

import boto3 as boto3
from botocore.exceptions import ClientError

from shared.const import PHOTOS_BUCKET, PRESIGNED_URL_EXPIRE_TIME
from shared.const import TEACHER_ID, EVENT_QUERY_STRING
from shared.hanlders.SpreadsheetHandler import SpreadsheetHandler
from shared.hanlders.TeacherHandler import TeacherHandler

s3_client = boto3.client("s3",
                         region_name="us-east-1",
                         aws_access_key_id=os.environ[
                             'S3_UPLOAD_AWS_ACCESS_KEY_ID'],
                         aws_secret_access_key=os.environ[
                             'S3_UPLOAD_AWS_SECRET_ACCESS_KEY']
                         )




@lambda_decorator
def get_attendance_spreadsheet(event, context):
    kindergarten_id = TeacherHandler.get_teacher_kindergarten_id(event[TEACHER_ID])

    current_month = datetime.now().strftime('%m')
    month = event[EVENT_QUERY_STRING]["month"] if "month" in event[
        EVENT_QUERY_STRING] else current_month
    month = month.zfill(2)
    attendance_report_data = SpreadsheetHandler.get_kindergarten_spreadsheet(kindergarten_id=kindergarten_id,
                                                                             month=month)

    with open("out.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(attendance_report_data)

    upload_file("out.csv", PHOTOS_BUCKET, f"{event[TEACHER_ID]}.csv")
    if os.path.isfile("out.csv"):
        os.remove("out.csv")

    url = s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': PHOTOS_BUCKET,
                'Key': f"{event[TEACHER_ID]}.csv"},
        ExpiresIn=PRESIGNED_URL_EXPIRE_TIME)

    return url


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

