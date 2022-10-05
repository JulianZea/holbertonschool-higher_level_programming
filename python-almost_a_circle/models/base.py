#!/usr/bin/python3
"""
Base class
"""
import json
import turtle


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
