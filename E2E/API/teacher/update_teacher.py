import requests
import json

from E2E.const import BASE_API_URL


def update_teacher_api(token, first_name, last_name,
                       kindergarten_id, kindergarten_name):
    payload = json.dumps({
        "last_name": last_name,
        "kindergarten_id": kindergarten_id,
        "kindergarten_name": kindergarten_name,
        "first_name": first_name
    })
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    return requests.request("PUT", f'{BASE_API_URL}/teacher/signup',
                            headers=headers,
                            data=payload)
