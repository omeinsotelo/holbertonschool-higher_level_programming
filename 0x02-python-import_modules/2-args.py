#!/usr/bin/python3
import sys
if __name__ == "__main__":
    contArg = len(sys.argv) - 1
    print("{:d}".format(contArg), end="")
    if contArg != 1:
        print(" {:s}".format("arguments"), end="")
    if contArg == 1:
        print(" {:s}".format("argument"), end="")
    if contArg == 0:
        print("{:s}".format("."))
    if contArg != 0:
        print("{:s}".format(":"))
    for i in range(1, contArg + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
