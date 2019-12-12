#!/usr/bin/python3
def remove_char_at(str, n):
    var = ""
    for i in range(0, len(str)):
        if i != n:
            var += str[i]
    return (var)
