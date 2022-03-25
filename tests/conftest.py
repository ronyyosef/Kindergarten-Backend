import os


def pytest_configure(config):
    os.environ['S3_UPLOAD_AWS_ACCESS_KEY_ID'] = ''
    os.environ['S3_UPLOAD_AWS_SECRET_ACCESS_KEY'] = ''
