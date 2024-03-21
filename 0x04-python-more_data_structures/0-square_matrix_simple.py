#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for line in matrix:
        square.append([x**2 for x in line])
    return square
