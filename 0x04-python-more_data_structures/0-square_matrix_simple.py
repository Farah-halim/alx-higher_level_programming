#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mmatrix = matrix.copy()
    y = len(matrix)
    for i in range(y):
        mmatrix[i] = list(map(lambda x: x**2, matrix[i]))
    return (mmatrix)
