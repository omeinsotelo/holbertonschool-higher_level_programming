#!/usr/bin/python3
"""
Function that prints a square with the character #.
size (int)

"""


def print_square(size):
    """
    Function that prints a square with the character #.
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for j in range(int(size)):
        print("#" * int(size))
