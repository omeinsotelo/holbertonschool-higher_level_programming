#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtx = [i[:] for i in matrix]
    index = 0
    for row in new_mtx:
        for col in row:
            row[index] = col * col
            index += 1
        index = 0
    return new_mtx
