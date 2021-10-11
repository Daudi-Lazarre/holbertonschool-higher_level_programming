#!/usr/bin/python3

def matrix_divided(matrix, div):
    matrix = []

    # Append these bad boys
    row_one = [1, 2, 3]
    row_two = [4, 5, 6]

    matrix.append(row_one)
    matrix.append(row_two)

    # Does not row one and row two 
    if not isinstance(row_one, (int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(row_two, (int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(row_one) != len(row_two):
        raise TypeError("Each row of the matrix must have the same size")

    div = ()

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    quotient = matrix / div

    return(round(quotient, 2))