import json
import requests

from E2E.const import BASE_API_URL


def update_teacher_name_api(token, first_name, last_name):
    payload = json.dumps({
        "first_name": first_name,
        "last_name": last_name
    })
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.request("PUT", f'{BASE_API_URL}/teacher/update_name',
                                headers=headers,
                                data=payload).json()
    return response
