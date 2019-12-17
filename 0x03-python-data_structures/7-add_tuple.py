#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    var1 = 0
    var2 = 0
    if tuple_a:
        if len(tuple_a) >= 2:
            var1 += tuple_a[0]
            var2 += tuple_a[1]
        elif len(tuple_a) == 1:
            var1 += tuple_a[0]
    if tuple_b:
        if len(tuple_b) >= 2:
            var1 += tuple_b[0]
            var2 += tuple_b[1]
        elif len(tuple_b) == 1:
            var1 += tuple_b[0]
    tuple_add = (var1, var2)
    return tuple_add
