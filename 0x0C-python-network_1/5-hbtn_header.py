#!/usr/bin/python3
"""Get header"""

import requests
import sys
from requests import get

if __name__ == "__main__":
    with requests.get(sys.argv[1]) as f:
        myHeader = f.get("X-Request-Id")
        print("{}".format(myHeader))
