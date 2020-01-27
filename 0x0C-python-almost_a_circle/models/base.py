#!/usr/bin/python3
"""Class Base """
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init constructor"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json dictionary"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Json String"""
        file = cls.__name__ + ".json"
        with open(file, "w") as nfile:
            if list_objs is None:
                nfile.write("[]")
            else:
                ndic = [i.to_dictionary() for i in list_objs]
                nfile.write(cls.to_json_string(ndic))
