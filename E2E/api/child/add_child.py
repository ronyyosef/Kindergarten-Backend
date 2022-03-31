import requests
import json

from E2E.const import BASE_API_URL


def add_child_api(token, first_name, last_name, parent1_phone_number,
                  parent2_phone_number, group_name):
    payload = json.dumps({
        "first_name": first_name,
        "last_name": last_name,
        "parent1_phone_number": parent1_phone_number,
        "parent2_phone_number": parent2_phone_number,
        "group_name": group_name
    })
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", f'{BASE_API_URL}/children',
                                headers=headers,
                                data=payload)
    return response
