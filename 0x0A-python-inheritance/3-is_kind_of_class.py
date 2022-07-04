#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ Method that returns True/False if obj is an
    instance of a_class
    Args:
        obj: object
        a_class: Super class
    Returns:
        True:  If obj is an instance
        FalseL If obj is not an instance
    """
    return isinstance(obj, a_class)
