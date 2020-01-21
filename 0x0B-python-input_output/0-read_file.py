#!/usr/bin/python3
""" Reads a text file """


def read_file(filename=""):
    """ Function that reads a text file """
    with open(filename, encoding='utf8') as f:
        for line in f:
            print(line, end="")
