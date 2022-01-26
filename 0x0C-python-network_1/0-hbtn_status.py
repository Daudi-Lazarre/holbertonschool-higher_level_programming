#!/usr/bin/python3
import urllib.request

link = "https://intranet.hbtn.io/status"

with urllib.request.urlopen(link) as f:
    myFile = f.read()

print("Body response:")
print("\t- type: {}".format(type(myFile)))
print("\t- content: {}".format(myFile))
print("\t- utf8 content: {}".format((myFile.decode("utf-8"))))
