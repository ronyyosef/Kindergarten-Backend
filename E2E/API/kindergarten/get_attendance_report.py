from E2E.const import BASE_API_URL
from urllib.parse import urlencode
from collections import OrderedDict
import requests


def get_attendance_report_api(token, month):
    headers = {
        'Authorization': token,
    }
    query_string = urlencode(OrderedDict(month=month))

    return requests.request(
        "GET",
        f'{BASE_API_URL}/kindergarten/attendance_spreadsheet?{query_string}',
        headers=headers)
