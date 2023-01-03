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

    # Error massages :)
    m_row_length = 'Each row of the matrix must have the same size'
    m = 'matrix must be a matrix (list of lists) of integers or floats'
    m_div = "matrix_divided() missing 1 required positional argument: 'div'"

    if (type(matrix) != list):
        raise TypeError(m)

    if div is None:
        raise TypeError(m_div)

    if (div == 0):
        raise ZeroDivisionError('division by zero')

    if ((type(div) != int) and (type(div) != float)):
        raise TypeError('div must be a number')

    n = len(matrix)

    # Confirm that matrix is a list of lists of integers or floats :)
    for l in range(n):
        if(type(matrix[l]) != list):
            raise TypeError(m)

    for l in range(n):
        if(type(matrix[l]) != list):
            raise TypeError(m)

        if (len(matrix[l]) > len(matrix[l-1])):
            raise TypeError(m_row_length)

        for j in range(len(matrix[l])):
            if (type(matrix[l][j]) != int) and (type(matrix[l][j]) != float):
                raise TypeError(m)

    if n > 1:
        new_matrix = [[], []]

    row = 0
    while row < n:
        for col in range(len(matrix[row])):
            new_matrix[row].append(round((matrix[row][col] / div), 2))

        row += 1

    return new_matrix
