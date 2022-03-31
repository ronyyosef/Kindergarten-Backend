from collections import OrderedDict
from urllib.parse import urlencode

import requests

from E2E.const import BASE_API_URL

url = "https://api.kindergartenil.com/kindergarten/exist?kindergarten_id=62f2f3ef"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


def get_kindergarten_exist_api(kindergarten_id):
    query_string = urlencode(OrderedDict(kindergarten_id=kindergarten_id))
    return requests.request(
        "GET",
        f'{BASE_API_URL}/kindergarten/exist?{query_string}',
        headers=headers)
