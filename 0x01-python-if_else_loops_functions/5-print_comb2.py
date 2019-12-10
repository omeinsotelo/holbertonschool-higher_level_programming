#!/usr/bin/python3
for i in range(0, 99):
        print("{:s}{:d}".format("0" if i < 10 else "", i), end=", ")
print("{:d}".format(99))
