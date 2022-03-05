import boto3 as boto3
from botocore.exceptions import ClientError

from const import PHOTOS_BUCKET, PRESIGNED_URL_EXPIRE_TIME

s3_client = boto3.client('s3')


class S3PhotosHandler:

    @staticmethod
    def get_photo_url(kindergarten_id, id):
        try:
            s3_client.head_object(Bucket='kindergarten-photos', Key=f'{kindergarten_id}/{id}.png')
        except ClientError:
            url = s3_client.generate_presigned_url(
                ClientMethod='get_object',
                Params={'Bucket': PHOTOS_BUCKET, 'Key': 'child_boy_default.jfif'},
                ExpiresIn=PRESIGNED_URL_EXPIRE_TIME)
        else:
            url = s3_client.generate_presigned_url(
                ClientMethod='get_object',
                Params={'Bucket': PHOTOS_BUCKET, 'Key': f'{kindergarten_id}/{id}.png'},
                ExpiresIn=PRESIGNED_URL_EXPIRE_TIME)
        return url

    @staticmethod
    def put_photo_url(kindergarten_id, id):
        # url = s3_client.generate_presigned_post(Bucket=PHOTOS_BUCKET,
        #                                         Key=f'{kindergarten_id}/{id}',
        #                                         Fields={"Content-Type": "image/jpg"},
        #                                         Conditions=["Content-Range: bytes */1000"],
        #                                         ExpiresIn=3600)
        url = boto3.client('s3').generate_presigned_url(
            ClientMethod='put_object',
            Params={'Bucket': PHOTOS_BUCKET, 'Key': f'{kindergarten_id}/{id}'},
            ExpiresIn=PRESIGNED_URL_EXPIRE_TIME)
        return url
