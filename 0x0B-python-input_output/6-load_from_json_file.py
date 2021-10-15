#!/usr/bin/python3#!/usr/bin/python3
""" writes an Object to a text file, using a JSON representation: """


import json

def save_to_json_file(my_obj, filename):
    """ obj to txt file  """
    
    with open(filename, mode='w', encoding="UTF-8") as file:
        save_Jason = json.loads(my_obj)
        file.write(save_Jason)
