#!/usr/bin/python3
"""Class based on 6-base_geometry.py"""


class BaseGeometry:
    """ Class defines the attributes of Geometric Shapes """

    def area(self):
        """ Method defines the area of a geomtric shape """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method recieves the value property

        Árgs:
            name: name of the object
            value: value of the property

        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
