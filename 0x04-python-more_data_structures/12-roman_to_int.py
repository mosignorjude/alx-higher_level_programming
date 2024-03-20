#!/usr/bin/python3
def roman_to_int(roman_string):
    rm_dict = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
               'IV': 3, 'IX': 8}
    num = 0
    total_num = 0
    prev_str = ''
    for i in roman_string:
        if i in rm_dict:
            if i == 'V' and prev_str == 'I':
                num = rm_dict['IV']
            elif i == 'X' and prev_str == 'I':
                num = rm_dict['IX']
            num = rm_dict[i]
            total_num += num
            prev_str = i
    return total_num
