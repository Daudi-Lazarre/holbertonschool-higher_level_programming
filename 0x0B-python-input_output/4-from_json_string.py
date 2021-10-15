#!/usr/bin/python3
""" returns an object (Python data structure) represented by a JSON string: """
import json


def from_json_string(my_str):
    """ From Rob Jecque'd to Jason """

    return(json.loads(my_str))
