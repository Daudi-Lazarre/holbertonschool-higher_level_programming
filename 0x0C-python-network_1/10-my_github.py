#!/usr/bin/python3
"Get to my Github"

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pw = sys.argv[2]

    req = requests.get("https://api.github.com/user",
                       auth=(user, pw))

    print(req.json().get("id"))
