#!/usr/bin/python3
class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """ Def area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validates value"""
        if not type(value) == int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
