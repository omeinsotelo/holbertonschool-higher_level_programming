#!/usr/bin/python3
"""
Class rectangle
"""


class Rectangle:
    """
    Class rectangle
    """

    def __init__(self, width=0, height=0):
        """
        constructor of instance
        """
        self.height = height
        self.width = width
    
    @property
    def width(self):
        """
        get width rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        get the heigth
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        set the heigth
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the rectangle area
        """
        return self.__width * self.__height 

    def perimeter(self):
        """
        returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2
        
    def __str__(self):
        """
        get the rectangle stirng format
        """
        mul = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                mul += "#" * self.__width
                mul += "\n"

        return mul
