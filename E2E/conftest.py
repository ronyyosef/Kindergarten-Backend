import os

os.environ['S3_UPLOAD_AWS_ACCESS_KEY_ID'] = ''
os.environ['S3_UPLOAD_AWS_SECRET_ACCESS_KEY'] = ''
import pytest
from E2E.clean_up import clean_up_e2e
from E2E.helpers.sign_in_user import authenticate_and_get_token
from E2E.helpers.sign_up_user import create_user
from E2E.model import Auth


def pytest_configure(config):
    print('before_tests')


# create new auth user
def get_user(username, password, app_client_id, user_pool_id) -> Auth:
    try:
        auth = authenticate_and_get_token(
            username=username,
            password=password,
            user_pool_id=user_pool_id,
            app_client_id=app_client_id)
    except BaseException:
        create_user(
            username=username,
            password=password,
            app_client_id=app_client_id, user_pool_id=user_pool_id)
        auth = authenticate_and_get_token(
            username=username,
            password=password,
            user_pool_id=user_pool_id,
            app_client_id=app_client_id)
    return auth


@pytest.fixture(scope='session', autouse=True)
def auth():
    password = '8277c30c-1880-4ada-b730-ec8f71a2bcec'
    username = '+972999999999'
    user_pool_id = 'us-east-1_PokjeshX3'
    app_client_id = '36d8opu7j2e9illge6vlfjdu9h'
    auth = get_user(username=username,
                    password=password,
                    app_client_id=app_client_id, user_pool_id=user_pool_id)
    yield auth
    # delete all
    clean_up_e2e(auth.teacher_id)
