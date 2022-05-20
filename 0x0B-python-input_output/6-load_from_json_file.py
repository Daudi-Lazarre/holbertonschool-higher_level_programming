#!/usr/bin/python3
"""
    Load from JSON
"""
import json


def load_from_json_file(filename):
    """Load from JSON file name"""
    with open(filename, 'r', encoding='utf-8') as fd:
        return(json.load(fd))
