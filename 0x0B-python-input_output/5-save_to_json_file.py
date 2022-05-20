#!/usr/bin/python3
"""
    Save JSON file
"""
import json


def save_to_json_file(my_obj, filename):
    """Save_to_json_file"""
    with open(filename, 'w', encoding='utf-8') as fd:
        return(json.dump(my_obj, fd))
