#!/usr/bin/python3
"""Error Code"""

import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as url:
            s = url.read()
            print(s.decode("utf-8"))

    except ValueError as message:
        message = urllib.error.HTTPError
        print("Error code: {}".format(message))
