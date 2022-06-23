#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two intergers
    Args are checked whether they are ints or floats and if not,
    TypeError is raised.
    Args are casted to ints if they are floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
