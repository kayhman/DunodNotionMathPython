from numpy import matrix

# La matrice à réorganiser est
# la martice A.
A = matrix([[1, 1, 1],
            [2, 2, 2],
            [3, 3, 3]])

# P est la matrice de permutation
# qui va échanger la ligne 1 avec la 2
# et inversement.
P = matrix([[0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]])

# La multiplication de A par P.
print(P.dot(A))
#> [[2 2 2]
#>  [1 1 1]
#>  [3 3 3]]
A = matrix([[1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]])

P = matrix([[0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]])

print(A.dot(P))
#> [[2 1 3]
#>  [2 1 3]
#>  [2 1 3]]


print(P.dot(A.dot(P)))
#> [[2 1 3]
#>  [2 1 3]
#>  [2 1 3]]
