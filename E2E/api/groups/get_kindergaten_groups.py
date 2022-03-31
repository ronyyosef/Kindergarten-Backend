import requests

from E2E.const import BASE_API_URL


def delete_group_api(token, group_name):

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    return requests.request("GET", f'{BASE_API_URL}/groups',
                            headers=headers)
