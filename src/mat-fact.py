from numpy import matrix, eye, zeros
from numpy.linalg import inv
# La matrice à factoriser
# est la matrice A.
A = matrix([[2, -1, 0],
            [-1, 2, -1],
            [0, -1, 2]])

L1 = matrix([[1, 0, 0],
             [1/2, 1, 0],
             [0, 0, 1]])
print(L1 * A)
# > [[ 2.  -1.   0. ]
#    [ 0.   1.5 -1. ]
#    [ 0.  -1.   2. ]]

L2 = matrix([[1, 0, 0],
             [0, 1, 0],
             [0, 2/3, 1]])
U = L2 * L1 * A
print(U)
#> [[ 2.         -1.          0.        ]
#   [ 0.          1.5        -1.        ]
#   [ 0.          0.          1.33333333]]

print(inv(L2 * L1))
#> [[ 1.          0.          0.        ]
#   [-0.5         1.          0.        ]
#   [ 0.         -0.66666667  1.        ]]

I = eye(3)
print(I - (L1 - I) - (L2 - I))
#> [[ 1.          0.          0.        ]
#   [-0.5         1.          0.        ]
#   [ 0.         -0.66666667  1.        ]]

L = I - (L1 - I) - (L2 - I)
print(L * U)
#> [[ 2. -1.  0.]
#   [-1.  2. -1.]
#   [ 0. -1.  2.]]

def LU_factorisation(M):
    I = eye(M.shape[0])
    L = eye(M.shape[0])
    for j in range(0, M.shape[0]):
        L_j = eye(M.shape[0])
        for i in range(j+1 , M.shape[0]):
            L_j[i, j] = -M[i, j] / M[j, j]
        M = L_j * M
        L = L - (L_j - I)
    return L, M

L, U = LU_factorisation(A)
print(L)
#> [[ 1.          0.          0.        ]
#   [-0.5         1.          0.        ]
#   [ 0.         -0.66666667  1.        ]]
print(U)
#> [[ 2.         -1.          0.        ]
#   [ 0.          1.5        -1.        ]
#   [ 0.          0.          1.33333333]]
print(L * U)
#> [[ 2. -1.  0.]
#   [-1.  2. -1.]
#   [ 0. -1.  2.]]

# Test sur une autre matrice
# de plus grande dimension
# et non symétrique.
A = matrix([[2, -1, 0, -3],
            [-1, 2, -1, 0],
            [0, -1, 2, -1],
            [-4, 0, -1, 2]])

L, U = LU_factorisation(A)
print(L)
#> [[ 1.          0.          0.          0.        ]
#   [-0.5         1.          0.          0.        ]
#   [ 0.         -0.66666667  1.          0.        ]
#   [-2.         -1.33333333 -1.75        1.        ]]
print(U)
#> [[ 2.         -1.          0.         -3.        ]
#   [ 0.          1.5        -1.         -1.5       ]
#   [ 0.          0.          1.33333333 -2.        ]
#   [ 0.          0.          0.         -9.5       ]]
print(L * U)
#> [[ 2. -1.  0. -3.]
#   [-1.  2. -1.  0.]
#   [ 0. -1.  2. -1.]
#   [-4.  0. -1.  2.]

# Grâce à la factorisation LU
# la résolution se code en peu de lignes.
def lu_solve(L, U, b):
    x =  zeros(b.shape[1])
    for idx, row in enumerate(L):
        x[idx] = (b[0, idx] - x.dot(row) ) / L[idx, idx]
    b = matrix([x])
    x =  zeros(b.shape[1])
    for idx in reversed(range(0, b.shape[1])):
        row = U[idx, :].T
        x[idx] = (b[0, idx] - x.dot(row) ) / U[idx, idx]

    return matrix([x]).T

b = matrix([[1, 2, 3, 4]])
x = lu_solve(L, U, b)

# En multipliant $A$ par $x$,
# $b$ apparaît.
print(A * x)
#> [[1.]
#   [2.]
#   [3.]
#   [4.]]
