#!/usr/bin/python3
""" Reads n lines of a text file and print it """


def read_lines(filename="", nb_lines=0):
    """ Function that read and print lines """
    total_lines = len(open(filename).readlines())
    if nb_lines <= 0 or nb_lines > total_lines:
        nb_lines = total_lines

    with open(filename, encoding='utf8') as file:
        for i in range(nb_lines):
            print(file.readline(), end="\n" if(i+1) == total_lines else "")
