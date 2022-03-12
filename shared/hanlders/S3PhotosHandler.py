import os

import boto3 as boto3
from botocore.exceptions import ClientError

from shared.const import PHOTOS_BUCKET, PRESIGNED_URL_EXPIRE_TIME

s3_client = boto3.client("s3",
                         region_name="us-east-1",
                         aws_access_key_id=os.environ[
                             'S3_UPLOAD_AWS_ACCESS_KEY_ID'],
                         aws_secret_access_key=os.environ[
                             'S3_UPLOAD_AWS_SECRET_ACCESS_KEY']
                         )


class S3PhotosHandler:
    @staticmethod
    def get_photo_url(kindergarten_id: str, id: str) -> str:
        try:
            s3_client.head_object(
                Bucket='kindergarten-photos',
                Key=f'{kindergarten_id}/{id}.png')
        except ClientError:
            url = None
        else:
            url = s3_client.generate_presigned_url(
                ClientMethod='get_object',
                Params={'Bucket': PHOTOS_BUCKET,
                        'Key': f'{kindergarten_id}/{id}.png'},
                ExpiresIn=PRESIGNED_URL_EXPIRE_TIME)
        return url

    @staticmethod
    def put_photo_url(kindergarten_id: str, id: str) -> str:
        response = s3_client.generate_presigned_post(
            Bucket=PHOTOS_BUCKET,
            Key=f'{kindergarten_id}/{id}.png',
            ExpiresIn=PRESIGNED_URL_EXPIRE_TIME,
            Fields={"Content-Type": "multipart/form-data"},
            Conditions=[
                ["content-length-range", 1,
                 5120000]])
        return response
