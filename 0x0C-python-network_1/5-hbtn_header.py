#!/usr/bin/python3
"""Get header"""

import requests
from requests import get
import sys


if __name__ == "__main__":
    print("{}".format(requests.get(sys.argv[1]).headers.get("X-Request-Id")))
