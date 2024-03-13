#!/usr/bin/python3
j_start = 0
for i in range(9):
    j_start += 1
    for j in range(j_start, 10):
        if i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}, ".format(i, j), end='')
