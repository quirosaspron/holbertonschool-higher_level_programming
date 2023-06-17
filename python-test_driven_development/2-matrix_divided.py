#!/usr/bin/python3
""" Module that divides a matrix"""


def matrix_divided(matrix, div):
    """Divides all the elements of the matrix by div"""
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if not isinstance(matrix[x][y], (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not all((len(x) == len(matrix[0]) for x in matrix)):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            matrix[x][y] = round(matrix[x][y] / div, 2)
    return (matrix)
