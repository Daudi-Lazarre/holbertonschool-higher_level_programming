#!/usr/bin/python3
import requests

with requests.fetch as f:
    fetch = requests.get("https://intranet.hbtn.io/status")
    myFile = f.read()

print("Body response:")
print("\t- type: {}".format(type(myFile)))
print("\t- content: {}".format(myFile))
print("\t- utf8 content: {}".format((myFile.decode("utf-8"))))
