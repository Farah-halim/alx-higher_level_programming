#!/usr/bin/python3
def uniq_add(my_list=[]):
    Sum = 0
    uniq_int = set(my_list)
    for i in uniq_int:
        Sum = Sum + i
    return (Sum)
