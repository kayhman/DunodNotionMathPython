import numpy as np

# Tetraèdre de référence.
X1 = np.array([0, 0, 0])
X2 = np.array([1, 0, 0])
X3 = np.array([0, 1, 0])
X4 = np.array([0, 0, 1])

# Fonctions d'interpolation
# pour chaque n\oe ud.
def f1(x, y, z):
    return 1 -x - y - z

def f2(x, y, z):
    return x

def f3(x, y, z):
    return y

def f4(x, y, z):
    return z

# Chaque fonction vaut 1
# pour son n\oe ud.
print(f1(X1[0], X1[1], X1[2]))
#> 1
print(f2(X2[0], X2[1], X2[2]))
#> 1
print(f3(X3[0], X3[1], X3[2]))
#> 1
print(f4(X3[0], X4[1], X4[2]))
#> 1

# Et 0.0 pour les autres.
print(f1(X2[0], X2[1], X2[2]))
#> 0
print(f2(X1[0], X1[1], X1[2]))
#> 0
print(f3(X2[0], X2[1], X2[2]))
#> 0
print(f4(X3[0], X3[1], X3[2]))
#> 0


# Tétraèdre quelconque.
X1 = np.array([1.1, 2, 3]).T
X2 = np.array([2, 2, 3]).T
X3 = np.array([1, 3, 3]).T
X4 = np.array([1, 2, 4]).T

# Matrice de changement
# de coordonnées.
M = np.matrix([X2 - X1,
               X3 - X1,
               X4 - X1]).T

# Fonctions d'interpolation
# pour chaque n\oe ud.
def f1(x, y, z):
    X = np.linalg.inv(M) * ([[x],  [y], [z]] - X1.reshape(3, 1))
    return (1 - X[0] - X[1] - X[2])[0,0]

def f2(x, y, z):
    X = np.linalg.inv(M) * ([[x],  [y], [z]] - X1.reshape(3, 1))
    return X[0,0]

def f3(x, y, z):
    X = np.linalg.inv(M) * ([[x],  [y], [z]] - X1.reshape(3, 1))
    return X[1,0]

def f4(x, y, z):
    X = np.linalg.inv(M) * ([[x],  [y], [z]] - X1.reshape(3, 1))
    return X[2,0]

# Chaque fonction vaut 1
# pour son n\oe ud dans le cas d'un tétraèdre quelconque.
print(f1(X1[0], X1[1], X1[2]))
#> 1
print(f2(X2[0], X2[1], X2[2]))
#> 1
print(f3(X3[0], X3[1], X3[2]))
#> 1
print(f4(X3[0], X4[1], X4[2]))
#> 1

# Et 0.0 pour les autres.
print(f1(X2[0], X2[1], X2[2]))
#> 0
print(f2(X1[0], X1[1], X1[2]))
#> 0
print(f3(X2[0], X2[1], X2[2]))
#> 0
print(f4(X3[0], X3[1], X3[2]))
#> 0
