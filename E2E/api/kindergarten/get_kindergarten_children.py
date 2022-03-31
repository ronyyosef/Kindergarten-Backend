import requests

from E2E.const import BASE_API_URL


def get_kindergarten_children_api(token):
    headers = {
        'Authorization': token,
    }

    return requests.request(
        "GET",
        f'{BASE_API_URL}/group_chidren',
        headers=headers)
