#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        co = add(a, b)
        for i in range(4, 6):
            co = add(co, i)
        return (co)
    else:
        return (sub(a, b))
