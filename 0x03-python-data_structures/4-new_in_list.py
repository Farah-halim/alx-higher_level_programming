#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listt = my_list.copy()
    counter = len(listt) - 1
    if idx < 0 or idx > counter:
        return my_list
    if idx <= counter:
        listt[idx] = element
    return listt
