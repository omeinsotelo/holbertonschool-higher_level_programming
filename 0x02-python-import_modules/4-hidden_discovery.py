#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    for i in range(0, len(names)):
        if names[i].find("__") == -1:
            print("{:s}".format(names[i]))
