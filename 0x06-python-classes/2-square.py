#!/usr/bin/python3
class Square:
    """Empty class square"""

    def __init__(self, sizeSquare=0):
        """init square function"""
        if not isinstance(sizeSquare, int):
            raise TypeError("size must be an integer")
        elif sizeSquare < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__sizeSquare = sizeSquare
