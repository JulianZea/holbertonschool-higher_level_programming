#!/usr/bin/python3
"""Function div matrix"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix."""
    if matrix:
        new_matrix = []
        for row in matrix:
            if div == 0:
                raise ZeroDivisionError('division by zero')
            elif type(div) not in (int, float):
                raise TypeError('div must be a number')
            else:
                new_matrix.append([round((n / div), 2) for n in row])
                return new_matrix

    for row in matrix:
        if type(matrix) not in (int, float):
            raise TypeError
            ('matrix must be a matrix (list of lists) of integers/floats')
        elif len(matrix) > matrix[row]:
            raise TypeError
            ('Each row of the matrix must have the same size')
