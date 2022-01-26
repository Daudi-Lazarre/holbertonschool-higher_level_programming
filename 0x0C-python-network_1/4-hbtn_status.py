#!/usr/bin/python3
""" Holberton status """
import requests

fetch = requests.get("https://intranet.hbtn.io/status")

print("Body response:")
print("\t- type: {}".format(type(fetch.text)))
print("\t- content: {}".format(fetch.text))
