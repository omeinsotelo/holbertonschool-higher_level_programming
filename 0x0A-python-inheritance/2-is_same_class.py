#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ Function that returns True if the object \
        is exactly an instance of the specified class
    """
    return True if type(obj) == a_class else False
