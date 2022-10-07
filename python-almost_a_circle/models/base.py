#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """
    First class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        self.id = id

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        sharing data representation
        """
        if list_dictionaries:
            dict = json.dumps(list_dictionaries)
            return(dict)
        return('[]')
