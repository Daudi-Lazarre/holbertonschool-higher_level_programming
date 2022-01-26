#!/usr/bin/python3
"""Get header"""

import requests
import sys

if __name__ == "__main__":
    with requests.get(sys.argv[1]) as f:
        myHeader = f.getheader("X-Request-Id")
        print("{}".format(myHeader))
