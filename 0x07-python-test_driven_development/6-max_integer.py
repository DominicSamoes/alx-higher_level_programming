#!/usr/bin/python3
def max_integer(list=[]):
    """Returns the largest integer from a list of integers
    Return:
        Max  integer
        None if list is empty
    """

    if (len(list) == 0):
        return (None)
    res = list[0]
    counter = 1
    while counter < len(list):
        if list[counter] > res:
            res = list[counter]
        counter += 1
    return (res)
