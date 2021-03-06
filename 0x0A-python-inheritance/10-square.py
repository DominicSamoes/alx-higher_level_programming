#!/usr/bin/python3
"""Class inherits from Task 9"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class defines a Square from Rectangle class """
    def __init__(self, size):
        """ Method initialises a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method returns a string with the area """
        return super().area()
