#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """Multiply two matrices
        Args:
            m_a: matrix a
            m_b: matrix b

        Returns:
            Product of matrices
        Raises:
            TypeError: If m_a or m_b is not a list
            If m_a or m_b is not a list of lists
            If one element of those list of lists is not
            an integer or a float
            If m_a or m_b is not a rectangle (all ‘rows’
            should be of the same size)
            ValueError: If  m_a or m_b is empty (it means: = [] or = [[]])
                        If m_a and m_b can’t be multiplied
    """

    val_err_a = "m_a can't be empty"
    val_err_b = "m_b can't be empty"
    type_err_a = "m_a must be a list"
    type_err_b = "m_b must be a list"

    if m_a == [] or m_a == [[]]:
        raise ValueError(val_err_a)
    if m_b == [] or m_b == [[]]:
        raise ValueError(val_err_b)

    if not isinstance(m_a, list):
        raise TypeError(type_err_a)
    if not isinstance(m_b, list):
        raise TypeError(type_err_b)

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
