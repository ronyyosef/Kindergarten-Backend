import requests

from E2E.const import BASE_API_URL


def get_child_api(token, child_id):
    headers = {
        'Authorization': token,
    }

    response = requests.request(
        "GET",
        f'{BASE_API_URL}/children?id={child_id}',
        headers=headers
    ).json()
    return response
