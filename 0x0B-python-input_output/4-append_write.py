#!/usr/bin/python3
""" Appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ Function appends string return char add """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
