import requests

from E2E.const import BASE_API_URL


def get_kindergarten_groups_api(token):

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    return requests.request("GET", f'{BASE_API_URL}/groups',
                            headers=headers).json()
