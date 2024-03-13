#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s_str = "Last digit of"
last_digit = 0

if number >= 0:
    last_digit = number % 10
elif number < 0:
    num = -1 * number
    last_digit = num % 10
    last_digit = -last_digit

if last_digit > 5:
    print("{} {:d} is {:d} and is greater than 5".format(s_str, number,
                                                         last_digit))
elif last_digit == 0:
    print("{} {:d} is {:d} and is 0".format(s_str, number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("{} {:d} is {:d} and is less than 6 and not 0".format(s_str, number,
                                                                last_digit))
