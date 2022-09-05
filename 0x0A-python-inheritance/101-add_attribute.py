#!/usr/bin/python3
"""Checks if an attributye can be added to an object"""


def add_attribute(an_obj, an_attr, a_value):
    """Checks if an_attr of a_value can be added to an_obj
    Args:
        an_obj: Object to add an attribute
        an_attr: Name of the attribute to add to object
        a_value: The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(an_obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(an_obj, an_attr, a_value)
