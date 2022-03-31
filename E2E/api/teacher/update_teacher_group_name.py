import requests
import json

from E2E.const import BASE_API_URL


def update_teacher_group_name_api(token, group_name):
    payload = json.dumps({
        "group_name": group_name
    })
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    return requests.request("PUT", f'{BASE_API_URL}/teacher/update_group_name',
                            headers=headers,
                            data=payload).json()
