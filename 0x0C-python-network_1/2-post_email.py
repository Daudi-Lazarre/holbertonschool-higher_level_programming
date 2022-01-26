#!/usr/bin/python3
"""How to post an email"""

import urllib.request
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    encode = urllib.parse.urlencode({"email": email}).encode('ascii')
    with urllib.request.urlopen(sys.argv[1], encode) as email:
        s = email.read()
        print(s.decode("utf-8"))
