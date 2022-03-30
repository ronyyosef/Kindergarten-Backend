import requests
import json

from E2E.const import BASE_API_URL


def get_teacher_api(token, child_id, group_name):
    payload = json.dumps({
        "child_id": child_id,
        "group_name": group_name
    })
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", f'{BASE_API_URL}/teacher',
                                headers=headers,
                                data=payload)
    return response
