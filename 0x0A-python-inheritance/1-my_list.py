#!/usr/bin/python3
class MyList(list):
    """ MyList class inherits from list """
    def print_sorted(self):
        """
        Function prints list in ascending sort
        """
        print(sorted(self))
