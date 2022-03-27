import requests

from E2E.const import BASE_API_URL


def get_teacher_api(token):
    payload = {}
    headers = {
        'Authorization': token,
    }

    response = requests.request("GET", f'{BASE_API_URL}/teacher',
                                headers=headers,
                                data=payload)
    return response
