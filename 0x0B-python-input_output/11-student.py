#!/usr/bin/python3
"""Class Student that defines a student"""


class Student:
    """Defines a student
    Public attributes:
        - first_name
        - last_name
        - age
    Public method to_json()
    """

    def __init__(self, first_name, last_name, age):
        """Initialise student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dict representation of Student instance
        Args:
            attrs: list of attributes
        Returns:
            the dict representation
        """
        my_dict = dict()
        if attrs and all(isinstance(a, str) for a in attrs):
            for a in attrs:
                if a in self.__dict__:
                    my_dict.update({a: self.__dict__[a]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attrs of the Student instance
        Args:
            json: dict of attrs
        """
        for a in json:
            self.__dict__.update({a: json[a]})
