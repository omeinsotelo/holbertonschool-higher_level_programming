#!/usr/bin/python3
"""
fn that prints a txt with 2 new lines after each of these char: ., ? and :
text (str)

"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each charac . ? :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    text = text.strip()
    count = 0

    while count < len(text):
        if text[count] in ".?:":
            print("{:s}".format(text[count]), end="\n\n")
            text = text[count + 1:]
            text = text.strip()
            count = 0
        else:
            print("{:s}".format(text[count]), end="")
            count += 1
