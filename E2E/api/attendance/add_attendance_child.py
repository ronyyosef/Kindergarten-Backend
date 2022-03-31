import requests
import json

from E2E.const import BASE_API_URL


def add_attendance_child_api(token, child_id, is_present):
    payload = json.dumps({
        "id": child_id,
        "is_present": is_present
    })
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    return requests.request("POST", f'{BASE_API_URL}/attendance',
                            headers=headers,
                            data=payload).json()
