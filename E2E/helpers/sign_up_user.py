import uuid

import boto3


def create_user(username: str, password: str,
                app_client_id: str) -> None:
    client = boto3.client('cognito-idp')

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
    print("User created successfully")
