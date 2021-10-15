#!/usr/bin/python3#!/usr/bin/python3
""" creates an Object from a “JSON file”: """


import json

def save_to_json_file(my_obj, filename):
    """ def load_from_json_file(filename): """
    
    with open(filename, mode='w', encoding="UTF-8") as file:
        save_Jason = json.loads(my_obj)
        file.write(save_Jason)


# You don’t need to manage exceptions if the JSON string doesn’t represent an object.
# You don’t need to manage file permissions / exceptions.