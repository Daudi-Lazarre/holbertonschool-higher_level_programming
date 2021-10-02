#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for j in row:
            matrixLength = len(row)
            i += 1
            print("{:d}".format(j), end="")
            if i != matrixLength:
                print(" ", end="")
        print("")
