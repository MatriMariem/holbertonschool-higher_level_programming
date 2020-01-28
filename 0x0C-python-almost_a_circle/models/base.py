#!/usr/bin/python3
"""
This module contains one class: Base
"""
import json


class Base:
    """
    The goal of this class is:
    to manage id attribute in all our future classes
    and to avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiation """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list_objs))
            



