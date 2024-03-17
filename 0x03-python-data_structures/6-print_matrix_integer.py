#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        i = 0
        while i < len(rows):
            print("{:d}".format(rows[i]) + " " if i != len(rows) - 1
                  else rows[i], end='')
            i += 1
        print()
