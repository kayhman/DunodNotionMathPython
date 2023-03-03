import numpy as np

# La matrice A contient
# notre système.
A = [[2, 1,    1, -1],
     [0, 1.5, -1,  0],
     [0, 0,    3, -1],
     [0, 0,    0,  1]]

# la matrice colonne B
# contient le terme de droite
B = [0, 0, 2, 43]

# La fonction Gauss Seidel
# calcule une solution approchée
# de notre système.
def gaussSeidel(A, B, maxIter):
    nligsA, ncolsA = len(A), len(A[0])
    X = [0.0] * ncolsA

    for j in range(0, maxIter):
        for i in range(0, ncolsA):
            X[i] = 0
            X[i] = (B[i] - np.dot([col for col in A[i]], X)) / A[i][i]
    return X

# Avec une seule itération
# on est loin du résultat.
print(gaussSeidel(A, B, 1))
# > [0.0, 0.0, 0.666, 43.0]
# Avec une de plus
# on se rapproche
print(gaussSeidel(A, B, 2))
# > [21.166666666666668, 0.4444444444444444, 15.0, 43.0]

# et deux de plus
# suffisent à trouver la
# solution exacte.
print(gaussSeidel(A, B, 4))
# > [9.0, 10.0, 15.0, 43.0]
