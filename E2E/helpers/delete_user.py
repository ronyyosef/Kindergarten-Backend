import boto3


def delete_user(username: str,
                user_pool_id: str):
    client = boto3.client('cognito-idp')
    client.admin_delete_user(
        UserPoolId=user_pool_id,
        Username=username
    )
    print('User deleted')
