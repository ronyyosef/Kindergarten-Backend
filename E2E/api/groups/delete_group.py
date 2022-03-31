import requests
import json

from E2E.const import BASE_API_URL


def delete_group_api(token, group_name):
    payload = json.dumps({
        "group_name": group_name
    })
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    return requests.request("POST", f'{BASE_API_URL}/groups/delete',
                            headers=headers,
                            data=payload).json()
