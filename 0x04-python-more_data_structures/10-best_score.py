#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    c = 0
    key = None
    for k in a_dictionary:
        if c >= a_dictionary[k]:
            continue
        elif c < a_dictionary[k]:
            c = a_dictionary[k]
            key = k
    return key
