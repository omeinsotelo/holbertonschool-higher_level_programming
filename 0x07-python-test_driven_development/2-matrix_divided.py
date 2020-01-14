#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
matrix (int, float)
div (int, float)
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """
    msj = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError(msj)

    for row in matrix:
        if type(row) != list:
            raise TypeError(msj)

    for row in matrix:
        for col in row:
            if type(col) != int and type(col) != float:
                raise TypeError(msj)

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mtx = [i[:] for i in matrix]
    for i in range(len(new_mtx)):
        for j in range(len(new_mtx[i])):
            new_mtx[i][j] = round(new_mtx[i][j] / div, 2)
    return new_mtx
