#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if ((j + 1) != len(matrix[i])):
                print("{:s}".format(" "), end="")
        print("{:s}".format("\n"), end="")
