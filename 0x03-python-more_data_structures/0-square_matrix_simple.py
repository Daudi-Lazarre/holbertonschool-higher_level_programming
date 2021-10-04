#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        add = []
        for rows in matrix:
            add.append([n ** 2 for n in rows])
        return add