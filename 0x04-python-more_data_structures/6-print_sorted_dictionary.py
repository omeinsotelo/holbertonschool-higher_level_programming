#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = a_dictionary
    print('\n'.join('{}: {}'.format(k, v) for k, v in sorted(dic.items())))
