#!/usr/bin/python3
"""Base Model Class"""
import json

class Base:
    """Defines the base class.
    Attributes:
        __nb_objects: The number of instantiated bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor
        Args:
            id: Identityof Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries: List of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
