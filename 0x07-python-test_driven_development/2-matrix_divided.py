#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix


    Args:
        matrix: ints or floats
        div: number which divides the matrix

    Return:
        New matrix quotient rounded to 2 dp
    Raise:
        TypeError:
            If not a list of integers or floats
            If each row is not of the same size
            If there is a non int or float div
        ZeroDivisionError:
            If there is a div = 0
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_m = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_m)

    leng = 0

    for elem in matrix:
        if not elem or not isinstance(elem, list):
            raise TypeError(msg_m)

        if leng != 0 and len(elem) != leng:
            raise TypeError("Each row of the matrix must have the same size")

        for val in elem:
            if not type(val) in (int, float):
                raise TypeError(msg_m)

        leng = len(elem)

    lm = list(map(lambda m: list(map(lambda n: round(n / div, 2), m)), matrix))
    return (lm)
