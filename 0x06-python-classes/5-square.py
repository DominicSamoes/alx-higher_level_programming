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

    @property
    def size(self):
        """Method that returns size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter that returns size value of square obj"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


    def my_print(self):
        """Prints in stdout the square the character #"""
        if not self.__size:
            print()
        else:
            for a in range(self.__size):
                for b in range(self.__size):
                    print("#", end='')
                print()

