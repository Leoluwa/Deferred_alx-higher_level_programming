#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        pass
    else:
        for u in range(len(matrix)):
            for length in range(len(matrix[u])):
                if length == (len(matrix[u]) - 1):
                    print("{:d}".format(matrix[u][length]), end='')
                else:
                    print("{:d}".format(matrix[u][length]), end=' ')
            print()
