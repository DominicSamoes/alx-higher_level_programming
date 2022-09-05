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

    def to_json(self):
        """Retrieves dict representation of Student instance
        Returns:
            the dict representation
        """
        return self.__dict__
