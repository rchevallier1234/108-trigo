## this file contains the functions performing the calculations
## for the different EXP COS SIN ARCCOS ARCSIN option
## and a function to display the matrix

from math import *
from opt_matrix import *
from create_matrix import *

def print_array(A, size):
    for i in range(size):
        for j in range(size):
            if (j == size - 1):
                print("{:.2f}".format(A[i][j]), end="")
            else:
                print("{:.2f}".format(A[i][j]), end="\t")
        print() 

def EXP(A, size):
    result = creat_matrix_identite(size)
    puissance = A
    for i in range(1, 80):
        result = add_matrix(result, div_matrix(puissance, i, size), size)
        puissance = multiply_matrix(puissance, A, size)
    return result

def COS(A, size):
    result = creat_matrix_identite(size)
    for i in range(1, 50):
        if i % 2 == 0:
            result = add_matrix(result, div_matrix(pow_matrix(A, 2 * i, size), factorial(2 * i), size), size)
        else:
            result = sub_matrix(result, div_matrix(pow_matrix(A, 2 * i, size), factorial(2 * i), size), size)
    print_array(result, size)
    return A

def SIN(A, size):
    result = A
    for i in range(1, 80):
        if i % 2 == 0:
            result = add_matrix(result, div_matrix(pow_matrix(A, 2 * i + 1, size), factorial(2 * i + 1), size), size)
        else:
            result = sub_matrix(result, div_matrix(pow_matrix(A, 2 * i + 1, size), factorial(2 * i + 1), size), size)
    print_array(result, size)
    return A

def HCOS(A, size):
    result = div_matrix(add_matrix(EXP(A, size), EXP(multiply_matrix2(-1, A, size) , size), size), 2, size)
    print_array(result, size)
    return result

def HSIN(A, size):
    result = div_matrix(sub_matrix(EXP(A, size), EXP(multiply_matrix2(-1, A, size) , size), size), 2, size)
    print_array(result, size)
    return A