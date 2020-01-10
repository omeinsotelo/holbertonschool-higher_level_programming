#!/usr/bin/python3
class Square:
    """Empty class square"""

    def __init__(self, size=0):
        """init square function"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Get the size"""
        return self.__size

    @size.setter
    def size(self, newSize):
        """Get the size"""
        if not isinstance(newSize, int):
            raise TypeError("size must be an integer")
        elif newSize < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = newSize

    def area(self):
        """Get the area"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square."""
        i = 0
        for i in range(self.__size):
            print("{}".format("#" * self.__size))
        if i == 0:
            print()
