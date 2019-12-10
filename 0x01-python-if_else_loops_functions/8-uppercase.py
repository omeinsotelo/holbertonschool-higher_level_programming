#!/usr/bin/python3
def uppercase(str):
        for i in range(0, len(str)):
                upper = ord(str[i])
                print("{:c}".format(upper - 32 if upper > 95 else upper), end="")
        print("{:s}".format("\n"), end="")
