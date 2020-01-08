#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(x):
        k = my_list[i]
        try: 
            print("{:d}".format(k), end="")
            j += 1
        except:
            pass
    print("")
    return j