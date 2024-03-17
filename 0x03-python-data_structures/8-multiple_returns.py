#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len == 0:
        first_char = None
        str_tuple = str_len, first_char
        return str_tuple
    else:
        first_char = sentence[0]
        str_len = len(sentence)
        str_tuple = str_len, first_char
        return str_tuple
