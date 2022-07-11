#!/usr/bin/python3
"""First class"""


class Base:
    """Defines the base class.
    Attributes:
        __nb_objects: The number of instantiated bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor
        Args:
            id: Identityof Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
