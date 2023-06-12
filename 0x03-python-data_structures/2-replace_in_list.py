#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    counter = len(my_list) - 1
    if idx < 0 or idx > counter:
        return my_list
    if idx <= counter:
        my_list[idx] = element
    return my_list
