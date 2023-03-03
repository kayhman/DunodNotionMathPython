import numpy as np

# Les cofacteurs sont les éléments $i, j$
# de la comatrice de A.
def cofactor(A, i, j):
    C_ij = A.copy()
    C_ij[:, j] = 0
    C_ij[i, j] = 1
    return np.linalg.det(C_ij)

# La comatrice regroupe les cofacteurs.
def comatrix(A):
    C = np.zeros(A.shape)
    for i in range(0, A.shape[0]):
        for j in range(0, A.shape[1]):
            C[i, j] = cofactor(A, i, j)
    return C

# L'inversion se fait de manière directe
# avec la formule donnée ci-contre.
def inv(A):
    return 1.0 / np.linalg.det(A) * comatrix(A).T


A = np.matrix([[2, -1, 0],
               [-1, 2, -1],
               [0, -1, 2]])

# l'inverse est bien celle attendue.
print(inv(A))
#> [[0.75 0.5  0.25]
#   [0.5  1.   0.5 ]
#   [0.25 0.5  0.75]]

# Il est facile de le vérifier avec numpy.
print(np.linalg.inv(A))
#> [[0.75 0.5  0.25]
#   [0.5  1.   0.5 ]
#   [0.25 0.5  0.75]]

print(inv(A) * A)
#> [[ 1.00000000e+00  1.11022302e-16  0.00000000e+00]
#   [ 0.00000000e+00  1.00000000e+00  0.00000000e+00]
#   [-5.55111512e-17  1.11022302e-16  1.00000000e+00]]


# Calcul de l'inverse en résolvant le système
# pour chacune des colonnes de la matrice identité.
I = np.eye(A.shape[0])
inv_1 = np.linalg.solve(A, I[:, 0])
# Le résultat est bien la première colonne.
print(inv_1)
#> [0.75 0.5  0.25]

inv_2 = np.linalg.solve(A, I[:, 1])
# Le résultat est bien la seconde colonne.
print(inv_2)
#> [0.5 1.  0.5]

inv_3 = np.linalg.solve(A, I[:, 2])
# Le résultat est bien la troisième colonne.
print(inv_3)
#> [0.25 0.5  0.75]
inv = np.matrix([inv_1, inv_2, inv_3]).T

# et le tout est bien l'inverse.
print(inv)
#> [[0.75 0.5  0.25]
#   [0.5  1.   0.5 ]
#   [0.25 0.5  0.75]]
