#!/usr/bin/python3
class Square:
    """Empty class square"""

    def __init__(self, size=0, position=(0, 0)):
        """init square function"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """Get position"""
        return self._Square__position

    @position.setter
    def position(self, position):
        """Set position"""
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Get the area"""
        return self.__size * self.__size

    def my_print(self):
        """print a # square """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("{}{}".format(" " * self.position[0], "#" * self.__size))
