#!/usr/bin/python3
"""Class square inherits from Rectangel"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor
        Args:
            size: Size of the Square.
            x: x coordinate of the Square.
            y: y coordinate of the Square.
            id: Identity of the Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str special method """
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_xy + str_wh

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
