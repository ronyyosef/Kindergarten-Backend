import boto3 as boto3
from botocore.exceptions import ClientError

from shared.const import PHOTOS_BUCKET, PRESIGNED_URL_EXPIRE_TIME

s3_client = boto3.client('s3')


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
        url = s3_client.generate_presigned_url(
            ClientMethod='put_object',
            Params={'Bucket': PHOTOS_BUCKET,
                    'Key': f'{kindergarten_id}/{id}.png'},
            ExpiresIn=PRESIGNED_URL_EXPIRE_TIME)
        return url
