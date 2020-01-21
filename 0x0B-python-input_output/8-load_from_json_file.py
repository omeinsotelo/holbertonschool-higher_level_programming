#!/usr/bin/python3
""" Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """ Creates an Objet JSON """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
