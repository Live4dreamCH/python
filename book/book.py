# -*- coding: utf-8 -*-

from requests import get, post
# import json
from traceback import print_exc
import os


url = 'https://www.bqg5.cc/15_15776/8219563.html'

while url != 'https://www.bqg5.cc/15_15776/':
    my_headers = {
        'Sec-Fetch-Dest': 'document',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
    res = get(url, headers = my_headers)
    res = res.text
    print(res)