from collections import OrderedDict
from urllib.parse import urlencode

import requests

from E2E.const import BASE_API_URL


def add_attendance_child_api(token, child_id, month):
    headers = {
        'Authorization': token,
    }
    query_string = urlencode(OrderedDict(child_id=child_id, month=month))

    return requests.request(
        "GET",
        f'{BASE_API_URL}/attendance?{query_string}',
        headers=headers)
