import boto3

from shared.const import CHILD_ID, KINDERGARTEN_ID, DATE, GROUP_NAME, \
    TEACHER_ID, PHOTOS_BUCKET


def clean_cognito_user_pool():
    client = boto3.client('cognito-idp')
    user_pool_id = 'us-east-1_PokjeshX3'
    users_data = client.list_users(
        UserPoolId=user_pool_id,
        AttributesToGet=[]
    )['Users']
    for user_data in users_data:
        username = user_data['Username']
        client.admin_delete_user(
            UserPoolId=user_pool_id,
            Username=username
        )


def clean_all_dynamodb():
    # AttendanceData
    table = boto3.resource('dynamodb').Table('AttendanceData')
    data = table.scan()['Items']
    for item in data:
        table.delete_item(
            Key={
                CHILD_ID: item[CHILD_ID],
                DATE: item[DATE]
            })

    # ChildData
    table = boto3.resource('dynamodb').Table('ChildData')
    data = table.scan()['Items']
    for item in data:
        table.delete_item(
            Key={
                CHILD_ID: item[CHILD_ID],
                KINDERGARTEN_ID: item[KINDERGARTEN_ID]
            })

    # GroupsData
    table = boto3.resource('dynamodb').Table('GroupsData')
    data = table.scan()['Items']
    for item in data:
        table.delete_item(
            Key={
                KINDERGARTEN_ID: item[KINDERGARTEN_ID],
                GROUP_NAME: item[GROUP_NAME],
            })

    # KindergartenData
    table = boto3.resource('dynamodb').Table('KindergartenData')
    data = table.scan()['Items']
    for item in data:
        table.delete_item(
            Key={
                KINDERGARTEN_ID: item[KINDERGARTEN_ID]
            })

    # TeacherData
    table = boto3.resource('dynamodb').Table('TeacherData')
    data = table.scan()['Items']
    for item in data:
        table.delete_item(
            Key={
                TEACHER_ID: item[TEACHER_ID]
            })
    # TeacherData
    table = boto3.resource('dynamodb').Table('ParentData')
    data = table.scan()['Items']
    for item in data:
        table.delete_item(
            Key={
                'parent_id': item['parent_id']
            })

def clean_all_s3():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(PHOTOS_BUCKET)
    # suggested by Jordon Philips
    bucket.objects.all().delete()
