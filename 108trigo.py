#!/usr/bin/python3
import sys
from create_matrix import creat_matrix_identite2
from calc_matrix import *

## check if argv are valide return false if argv is not a nbr and if the number of index are less than 2
def isvalid_argv(argv):
    index = 0
    for i in argv:
        if (i.isnumeric() == False and i.find("-") == -1 and index >= 2):
            return False
        index += 1
    if (index <= 2):
        return False
    return True

## create a matrix from argv
def creat_matrix_from_argv(size):
    index = 2
    A = creat_matrix_identite2(size)
    for i in range(size):
        for j in range(size):
            A[i][j] = int(sys.argv[index])
            index += 1
            if (index == argc):
                return A
    print(A)
    return A

if (isvalid_argv(sys.argv) == False):
    sys.exit(84)
size = 1
argc = len(sys.argv)
while (size * size < argc - 2):
    size += 1
A = creat_matrix_from_argv(size)
if (sys.argv[1] == "EXP"):
    result = EXP(A, size)
    print_array(result, size)
elif (sys.argv[1] == "COS"):
    COS(A, size)
elif (sys.argv[1] == "SIN"):
    SIN(A, size)
elif (sys.argv[1] == "COSH"):
    HCOS(A, size)
elif (sys.argv[1] == "SINH"):
    HSIN(A, size)
else:
    sys.exit(84)
sys.exit(0)
