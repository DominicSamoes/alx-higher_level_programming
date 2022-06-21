#!/usr/bin/python3
class Square:
    """Define a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Init a new square
        
        Args:
            size (int): size of square
            position (int, int): position of square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Method that returns size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter that returns size value of square obj"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Method that returns position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter that sets the position value of a square object"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates area of square"""
        return (self.__size**2)

    def my_print(self):
        """Prints in stdout the square the character #"""
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for a in range(0, self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
