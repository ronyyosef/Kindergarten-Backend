import uuid

import pytest

from E2E.helpers.delete_user import delete_user
from E2E.helpers.sign_in_user import authenticate_and_get_token
from E2E.helpers.sign_up_user import create_user


def pytest_configure(config):
    print('before_tests')


@pytest.fixture(scope='session', autouse=True)
def user_auth():
    # Will be executed before the first test
    password = str(uuid.uuid1())
    username = '+972999999999'
    user_pool_id = 'us-east-1_PokjeshX3'
    app_client_id = '36d8opu7j2e9illge6vlfjdu9h'
    create_user(
        username=username,
        password=password,
        app_client_id=app_client_id)
    id_token = authenticate_and_get_token(
        username=username,
        password=password,
        user_pool_id=user_pool_id,
        app_client_id=app_client_id)
    yield id_token
    # Will be executed after the last test
    delete_user(username=username, user_pool_id=user_pool_id)


