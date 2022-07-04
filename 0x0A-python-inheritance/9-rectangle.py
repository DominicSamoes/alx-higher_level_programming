#!/usr/bin/python3
"""Class inherits from task based on 8-rectangle.py"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class defines a rectangle from BaseGeometry Class"""

    def __init__(self, width, height):
        """Initialises instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method returns the area of the instance"""
        return self.__width * self.__height

    def __str__(self):
        """Special method returns the printable string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
