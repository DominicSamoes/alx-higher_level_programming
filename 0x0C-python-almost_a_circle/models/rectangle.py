#!/usr/bin/python3
"""Class Rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances
        Args:
            width: Width of the Rectangle.
            height: Height of the Rectangle.
            x: The x coordinate of the Rectangle.
            y: The y coordinate of the Rectangle.
            id: Identity of the Rectangle/
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
