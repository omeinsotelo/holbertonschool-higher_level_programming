#!/usr/bin/python3
class Square:
    """Empty class square."""

    def __init__(self, size=0):
        """init square function"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Get the area"""
        return self.__size * self.__size
