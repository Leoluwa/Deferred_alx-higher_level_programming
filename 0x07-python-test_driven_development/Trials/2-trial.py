#!/usr/bin/python3
'''
 This is the '2-matrix_divided' module :)

 This module supplies one function called matrix_divided(matrix, div).
'''


def matrix_divided(matrix, div):
    '''
     This function takes two arguments ~ a matrix and a divisor.
     The matrix is a list of list, and the divisor is an integer.

     It divides each of the elements of the given matrix by the
     given divisor and the result (the quotient) of each division
     is stored in new matrix.

     It returns the new matrix :)
    '''

    l = type(matrix)

    if (l != list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    n  = len(matrix)

    if n > 1:
        new_matrix = [[], []]

    row = 0
    while row < n:
        for col in range(len(matrix[row])):
            new_matrix[row].append(round((matrix[row][col] / div), 2))

        row += 1

    return new_matrix

