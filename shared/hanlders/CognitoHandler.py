import jwt


class CognitoHandler:

    @staticmethod
    def get_teacher_id(event: dict) -> str:
        return jwt.decode(event["headers"]["Authorization"], options={
                          "verify_signature": False})['cognito:username']
