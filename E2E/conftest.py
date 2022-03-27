import os
import uuid
from typing import TypedDict

import pytest

from E2E.helpers.delete_user import delete_user
from E2E.helpers.sign_in_user import authenticate_and_get_token
from E2E.helpers.sign_up_user import create_user


def pytest_configure(config):
    print('before_tests')
    os.environ['S3_UPLOAD_AWS_ACCESS_KEY_ID'] = ''
    os.environ['S3_UPLOAD_AWS_SECRET_ACCESS_KEY'] = ''


# create new auth user
@pytest.fixture(scope='session', autouse=True)
def auth():
    password = str(uuid.uuid1())
    username = '+972999999999'
    user_pool_id = 'us-east-1_PokjeshX3'
    app_client_id = '36d8opu7j2e9illge6vlfjdu9h'
    create_user(
        username=username,
        password=password,
        app_client_id=app_client_id, user_pool_id=user_pool_id)
    auth = authenticate_and_get_token(
        username=username,
        password=password,
        user_pool_id=user_pool_id,
        app_client_id=app_client_id)
    yield auth
    # Will be executed after the last test
    delete_user(username=username, user_pool_id=user_pool_id)
