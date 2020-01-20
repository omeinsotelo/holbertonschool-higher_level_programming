#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ Function that returns True if the object is an instance
    of a class that inherited
    """
    return not (type(obj) == a_class) and isinstance(obj, a_class)
