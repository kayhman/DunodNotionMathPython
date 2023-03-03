# L'installation se fait avec pip : pip install numpy
# L'import de la librairie se fait avec
import numpy as np
# np devient un alias vers Numpy.

# Un vecteur se crée ainsi
v = np.array([1, 2, 3])
print(v)
#> [1 2 3]

# diverses opérations statistiques sont disponibles en standard.
print(v.sum())
#> 6
print(v.mean())
#> 2.0
print(v.std())
#> 0.816496580927726

# Une matrice est définie comme suit
M = np.matrix([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
print(M)
#> [[1 2 3]
#   [4 5 6]
#   [7 8 9]]
# Produit matrice vecteur
print(M.dot(v))
#inversion de matrice
M = np.matrix([[2, -1, 0],
               [-1, 2, -1],
               [0, -1, 2]])
print(np.linalg.inv(M))
#> [[0.75 0.5  0.25]
#   [0.5  1.   0.5 ]
#   [0.25 0.5  0.75]]
