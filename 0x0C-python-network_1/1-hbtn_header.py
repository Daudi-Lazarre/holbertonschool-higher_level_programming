#!/usr/bin/python3
"""Get header"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as f:
        myHeader = f.getheader("X-Request-Id")
        print("{}".format(myHeader))
        