import jwt


class CognitoHandler:

    @staticmethod
    def get_user_id(event: dict):
        return jwt.decode(event["headers"]["Authorization"], options={"verify_signature": False})['cognito:username']