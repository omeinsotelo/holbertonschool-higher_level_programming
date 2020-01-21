#!/usr/bin/python3
import json
""" Writes an Object to a text file, using a JSON """


def save_to_json_file(my_obj, filename):
    """ Function Writes an Object to a text file JSON """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(json.dumps(my_obj))
