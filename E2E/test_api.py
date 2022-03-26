from E2E.helpers.delete_user import delete_user
from E2E.helpers.sign_in_user import authenticate_and_get_token
from E2E.helpers.sign_up_user import create_user


def test_create_user(user_auth):
    password = "test1234"
    username = '+972999999999'
    user_pool_id = 'us-east-1_PokjeshX3'
    app_client_id = '36d8opu7j2e9illge6vlfjdu9h'
    # create_user(
    #     username=username,
    #     password=password,
    #     app_client_id=app_client_id)
    # id_token = authenticate_and_get_token(
    #     username=username,
    #     password=password,
    #     user_pool_id=user_pool_id,
    #     app_client_id=app_client_id)
    # delete_user(username=username, user_pool_id=user_pool_id)
    # print(id_token)
