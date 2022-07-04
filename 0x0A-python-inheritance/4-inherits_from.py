#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ Method that returns True/False if obj is an
    instance of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True: if obj is an instance
        False: if obj is not an instance
    """
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
