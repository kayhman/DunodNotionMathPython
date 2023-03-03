from sympy import symbols, solve, Matrix
import numpy as np

A = np.matrix([[2, -1, 0],
               [-1, 2, -1],
               [0, -1, 2]])

lambdas, eVs= np.linalg.eig(A)
# Valeurs propres.
print(lambdas)
#> [3.41421356 2.         0.58578644]
# Vecteurs propres.
print(eVs)
#> [[-5.00000000e-01 -7.07106781e-01  5.00000000e-01]
#   [ 7.07106781e-01  4.05405432e-16  7.07106781e-01]
#   [-5.00000000e-01  7.07106781e-01  5.00000000e-01]]

# L'inverse de la matrice contenant
# les vecteurs propres est
# sa transposée.
print(eVs * eVs.T)
#> [[1.00000000e+00 5.55111512e-17 0.00000000e+00]
#   [5.55111512e-17 1.00000000e+00 1.11022302e-16]
#   [0.00000000e+00 1.11022302e-16 1.00000000e+00]]

# La méthode des puissances itérées
# permet de calculer
# le vecteur propre
# associé à la plus grande valeur propre.
def power(A, b, n_iter=100):
    for i in range(0, n_iter):
        b = A * b
        b = b / np.linalg.norm(b)
    return b

# Application à la matrice A.
b = np.matrix([[1], [1], [1]])
eV1 = power(A, b)
x = A * eV1
# Recalcul de la valeur propre associée.
lambda1 = x[0, 0] / eV1[0,0]

# Le vecteur obtenu est bien le vecteur propre.
print(eV1)
#> [[ 0.5       ]
#   [-0.70710678]
#   [ 0.5       ]]

# La valeur propre est la bonne.
print(lambda1)
#> 3.414213562373095
# et $A e_1$
print(x)
#> [[ 1.70710678]
#  [-2.41421356]
#  [ 1.70710678]]
# est bien égale à $\lambda_1 e_1$.
print(lambda1 * eV1)
#> [[ 1.70710678]
#   [-2.41421356]
#   [ 1.70710678]]

# Le conditionnement de A
# est donné par :
c = max(lambdas) / min(lambdas)
print(c)
#> 5.8284271247461845
# ce qui est un bon conditionnement.

# Calcul des valeurs propres
# à l'aide du déterminant
# du polynôme caractéristique.
l = symbols("l")
I = np.eye(A.shape[0])

S = (Matrix(A) + l * Matrix(I))
lambdas = solve(S.det(), l)
print(lambdas)
#> [-3.41421356237309, -2.00000000000000, -0.585786437626905]
# Ce sont bien les valeurs propres attendues.
