#!/usr/bin/python3
def print_square(size):
    """Prints a square with the character #
    
    Args:
        size: length of the square

    Returns:
        No return

    Raises:
        TypeError: If size is a non integer value
                    If size is float and less than 0.
        ValueError: If size is less than zero.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
       for i in range(size):
           print("#" * size)
