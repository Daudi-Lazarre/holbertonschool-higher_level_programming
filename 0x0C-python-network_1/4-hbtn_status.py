#!/usr/bin/python3
import requests

fetch = requests.get("https://intranet.hbtn.io/status")

print("Body response:")
print("\t- type: {}".format(type(fetch)))
print("\t- content: {}".format(fetch))
