#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
            num += 1
    except IndexError:
        pass
    except TypeError:
        print("Invalid input")
    print()
    return (num)
