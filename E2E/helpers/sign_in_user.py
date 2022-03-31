import boto3
import jwt

from E2E.model import Auth


def authenticate_and_get_token(username: str, password: str,
                               user_pool_id: str, app_client_id: str) -> Auth:
    client = boto3.client('cognito-idp')

    resp = client.admin_initiate_auth(
        UserPoolId=user_pool_id,
        ClientId=app_client_id,
        AuthFlow='ADMIN_NO_SRP_AUTH',
        AuthParameters={
            "USERNAME": username,
            "PASSWORD": password
        }
    )

    print("Log in successfully")
    username = jwt.decode(resp['AuthenticationResult']['IdToken'], options={
        "verify_signature": False})['cognito:username']
    return Auth(**{'token': resp['AuthenticationResult']
                ['IdToken'], 'teacher_id': username})
