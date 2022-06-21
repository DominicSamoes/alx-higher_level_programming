#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Init a new square.

        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates area of square"""
        return(self.__size**2)
