#!/usr/bin/python3
""" Returns the number of lines of a text file """


def number_of_lines(filename=""):
    """ Function returns number lines """
    with open(filename, encoding='utf8') as file:
        return len(file.readlines())
