#!/usr/bin/python3
""" Holberton status """
from urllib import response
import requests

response = requests.get("https://intranet.hbtn.io/status")

print("Body response:")
print("\t- type: {}".format(type(response)))
print("\t- content: {}".format(response))
