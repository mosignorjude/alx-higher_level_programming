#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    total = 0
    for elements in my_set:
        total = total + elements
    return total
