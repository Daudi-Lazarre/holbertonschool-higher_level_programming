#!/usr/bin/python3
"""Error Code"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as url:
        s = url.read()

        message = urllib.error.HTTPError
        print(s.decode("utf-8"))
        print("Error code: {}".format(message))
