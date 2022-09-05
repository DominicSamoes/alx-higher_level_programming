#!/usr/bin/python3
"""Finds list of available attributes and methods"""


def lookup(obj):
    """Function that returns the list of available attributes
and methods of an object
    Args:
        obj: instance of class
    Returns:
        List of attributes and methods
    """

    return dir(obj)
