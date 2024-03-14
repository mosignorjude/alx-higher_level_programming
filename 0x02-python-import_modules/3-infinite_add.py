#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    sum = 0
    num_of_elements = len(argv)
    for i in range(1, num_of_elements):
        sum = sum + int(argv[i])

    print(sum)
