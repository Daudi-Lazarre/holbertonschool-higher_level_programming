#!/usr/bin/python3
"Get to my Github"

import requests
from requests import get
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    req = requests.get('https://api.github.com/users/', 
                        profile=(username, password))

    print(req.json().get("id"))
