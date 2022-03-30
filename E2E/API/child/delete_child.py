import requests
import json

from E2E.const import BASE_API_URL


def delete_child_api(token, child_id):
    payload = json.dumps({
        "id": child_id
    })
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", f'{BASE_API_URL}/children/delete',
                                headers=headers,
                                data=payload)
    return response
