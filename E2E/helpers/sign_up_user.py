import boto3

from E2E.helpers.delete_user import delete_user


def create_user(username: str, password: str,
                app_client_id: str, user_pool_id:str) -> None:
    client = boto3.client('cognito-idp')
    try:
        sign_up(app_client_id, client, password, username)
    except Exception:
        delete_user(username=username, user_pool_id=user_pool_id)
        sign_up(app_client_id, client, password, username)
    print("User created successfully")


def sign_up(app_client_id, client, password, username):
    client.sign_up(
        ClientId=app_client_id,
        Username=username,
        Password=password,
        UserAttributes=[
            {
                'Name': 'phone_number',
                'Value': username
            },
        ]
    )
