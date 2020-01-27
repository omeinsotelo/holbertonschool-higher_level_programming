#!/usr/bin/python3
"""Module class base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Get Area"""
        return self.__width * self.__height

    def display(self):
        """Gett Display"""
        stry = "\n" * self.__y
        strx = " " * self.__x
        strw = strx + ("#" * self.__width) + "\n"
        strh = stry + (strw * self.__height)
        print(strh, end="")

    def __str__(self):
        """Str Method"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.__x,
            self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update obj values"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Dictionary Method"""
        _key = ["id", "width", "height", "x", "y"]
        _tpl = []
        for i in _key:
            _tupla = (i, getattr(self, i))
            _tpl.append(_tupla)
        return dict(_tpl)
