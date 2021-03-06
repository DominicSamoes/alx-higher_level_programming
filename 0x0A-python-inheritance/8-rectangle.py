#!/usr/bin/python3
"""Class inherits from Task 7"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class defines a rectangle from BaseGeometry Class"""

    def __init__(self, width, height):
        """Initialises instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
