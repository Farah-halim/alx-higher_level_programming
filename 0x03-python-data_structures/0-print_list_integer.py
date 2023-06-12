#!/usr/bin/python3
def print_list_integer(my_list=[]):
    counter = len(my_list)
    for i in range(counter):
        print("{:d}".format(my_list[i]))
