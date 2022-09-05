#!/usr/bin/python3i
"""Creates a class inheriting from list class"""


class MyList(list):
    """ Class defines an inherited list class
    Args:
        list: class list
    """

    def print_sorted(self):
        """ Method prints the sorted list """
        print(sorted(self))
