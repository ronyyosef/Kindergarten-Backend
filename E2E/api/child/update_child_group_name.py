import requests
import json

from E2E.const import BASE_API_URL


def update_child_group_name_api(token, child_id, group_name):
    payload = json.dumps({
        "child_id": child_id,
        "group_name": group_name
    })
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", f'{BASE_API_URL}/children/update_group_name',
                                headers=headers,
                                data=payload).json()
    return response
