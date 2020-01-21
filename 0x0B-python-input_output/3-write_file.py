#!/usr/bin/python3
"""  Writes a string to a text file """


def write_file(filename="", text=""):
    """ Function writes a string return num char """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
