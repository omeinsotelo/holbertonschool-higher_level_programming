#!/usr/bin/python3
"""Reads a text file aun print"""


def read_file(filename=""):
    """Function read and print"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
