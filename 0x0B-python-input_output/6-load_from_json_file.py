#!/usr/bin/python3#!/usr/bin/python3
""" creates an Object from a “JSON file”: """


import json

def save_to_json_file(my_obj, filename):
    """ From Jason to object FILE """
    
    with open(filename) as file:
        save_Jason = json.loads(my_obj)
        file.write(save_Jason)
        return(save_Jason)
