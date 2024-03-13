#!/usr/bin/python3

def uppercase(str):
    for a in str:
        char_code = ord(a)
        if char_code >= 97 and char_code <= 122:
            char_code = char_code - 32
        print("{}".format(chr(char_code)), end='')
    print()
