#!/usr/bin/python3

def print_last_digit(number):
    last_digit = 0

    if number >= 0:
        last_digit = number % 10
    elif number < 0:
        num = -1 * number
        last_digit = num % 10
    print("{:d}".format(last_digit), end='')
    return last_digit
