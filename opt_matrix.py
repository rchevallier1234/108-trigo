## this file contains the functions performing 
## basic calculations on the matrix

from create_matrix import *

def div_matrix(A, i, size):
    for row in range(size):
        for j in range(size):
            A[row][j] /= i
    return A

def add_matrix(A, A2, size):
    result = creat_matrix_identite2(size)
    for i in range(size):
        for j in range(size):
            result[i][j] = A2[i][j] + A[i][j]
    return result

def sub_matrix(A, A2, size):
    result = creat_matrix_identite2(size)
    for i in range(size):
        for j in range(size):
            result[i][j] = A[i][j] - A2[i][j]
    return result

def pow_matrix(A, n, size):
    tab = A
    for a in range(n - 1):
        tab = multiply_matrix(tab, A, size)
    return (tab)

def multiply_matrix(A, A2, size):
    result = creat_matrix_identite2(size)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * A2[k][j]
    return result

def multiply_matrix2(A, A2, size):
    result = creat_matrix_identite2(size)
    for i in range(size):
        for j in range(size):
            result[i][j] += A * A2[i][j]
    return result