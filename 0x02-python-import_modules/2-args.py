#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    num_of_elements = len(argv)
    if num_of_elements <= 1:
        print("{} arguments.".format(num_of_elements - 1))
    elif num_of_elements == 2:
        print("{} argument:".format(num_of_elements - 1))
    else:
        print("{} arguments:".format(num_of_elements - 1))
    for i in range(1, num_of_elements):
        print("{}: {}".format(i, argv[i]))
