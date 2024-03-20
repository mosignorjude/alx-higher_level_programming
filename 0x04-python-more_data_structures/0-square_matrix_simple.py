#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for rows in matrix:
        squared_elem = [x**2 for x in rows]
        squared_matrix.append(squared_elem)
    return squared_matrix
