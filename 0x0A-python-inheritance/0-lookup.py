#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object
obj (object)

"""


def lookup(obj):
    """
    Function returns the list of available attributes and methods of an object
    """
    return dir(obj)
