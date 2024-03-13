#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
s_str = "Last digit of"

if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    print("{} {:d} is {:d} and is greater than 5".format(s_str, number,
    last_digit))
if last_digit == 0:
    print("{} {:d} is {:d} and is 0".format(s_str, number, last_digit))
if last_digit < 6 and not 0:
    print("{} {:d} is {:d} less than 6 and not 0".format(s_str, number,
                                                         last_digit))
