#!/usr/bin/python3#!/usr/bin/python3
""" creates an Object from a “JSON file”: """


import json

def load_from_json_file(filename):
    """ From Jason to object FILE """
    
    with open(filename) as file:
        save_Jason = json.loads(filename)
        return(save_Jason)
