#!/usr/bin/python3
"""Method returns a list of integers"""


def pascal_triangle(n):
    """Returns  list of list of integers representing the
    Pascal's triangle of n
    Args:
        n: size of Pascal's triangle
    Returns:
        list of lists of integers
    """
    if n <= 0:
        return []

    my_list = [[1]]
    while len(my_list) != n:
        triangle = my_list[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        my_list.append(temp)
    return my_list
