import numpy as np

# Nous créons ici deux vecteurs de dimension 3, A et B.
# Ce sont aussi des points.
A  = np.array([1, 0, 0])
B  = np.array([0, 1, 0])
print(A, B)
#> [1 0 0] [0 1 0]

# Il est possible de les sommer, de manière à construire S.
S = A + B
print(S)
#> [1 1 0]

# La multiplication entre vecteurs n'est pas possible,
# Par contre il est possible de les multiplier par un scalaire:
M = 0.5 * A
print(M)
#> [0.5 0 0]


# Multiplier deux vecteurs entre eux ne génère pas un vecteur
# mais un scalaire. On parle de produit scalaire, ou {\em dot product} en anglais.
s = A.dot(B)
print(s)
#> 0

# Le calcul du vecteur $\mathbf{v}$ entre
# $A$ et $B$ se realise comme suit :
v = B - A
print(v)
#> [-1 1 0]
