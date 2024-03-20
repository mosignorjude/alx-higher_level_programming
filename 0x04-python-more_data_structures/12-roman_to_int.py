#!/usr/bin/python3
def roman_to_int(roman_string):
    rm_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    total_num = 0
    prev_num = 0
    if roman_string is None:
        return 0
    for i in roman_string:
        if i in rm_dict:
            if prev_num == 0:
                prev_num = rm_dict[i]
            if rm_dict[i] > prev_num:
                num = rm_dict[i] - prev_num - 1
            else:
                num = rm_dict[i]
            total_num += num
            prev_num = num
        else:
            return 0
    return total_num
