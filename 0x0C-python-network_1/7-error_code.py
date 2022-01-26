#!/usr/bin/python3
"""Error Code"""

import requests
import sys

if status_code >= 400:
    try:
        with requests(sys.argv[1]) as url:
            s = url.read()
            print(s.decode("utf-8"))

    except requests as message:
        print(message.text)
