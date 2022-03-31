import requests

from E2E.const import BASE_API_URL


def get_kindergarten_info_api(token):
    headers = {
        'Authorization': token,
    }

    return requests.request(
        "GET",
        f'{BASE_API_URL}/kindergarten/info',
        headers=headers).json()
