import sys

## create the identite matrix
## {1 0 0}
## {0 1 0}
## {0 0 1}

def creat_matrix_identite(size):
    tmp = []
    for i in range(size):
        tab = []
        for j in range(size):
            tab.append(1 if j == i else 0)
        tmp.append(tab)
    return tmp

## create the identite matrix
## {0 0 0}
## {0 0 0}
## {0 0 0}

def creat_matrix_identite2(size):
    tmp = []
    for i in range(size):
        tab = []
        for j in range(size):
            tab.append(0)
        tmp.append(tab)
    return tmp