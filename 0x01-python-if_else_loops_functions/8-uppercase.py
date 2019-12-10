#!/usr/bin/python3
def uppercase(str):
        for i in range(0, len(str)):
                upp = ord(str[i])
                print("{:c}".format(upp - 32 if upp > 95 else upp), end="")
        print("{:s}".format("\n"), end="")
