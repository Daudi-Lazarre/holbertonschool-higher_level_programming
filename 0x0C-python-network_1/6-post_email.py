#!/usr/bin/python3
"""How to post an email"""

import requests
import sys

if __name__ == "__main__":

    email = sys.argv[2]
    req = requests.post(sys.argv[1], data={"email": email})
    print(req.text)
