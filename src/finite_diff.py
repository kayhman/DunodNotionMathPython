import matplotlib.pyplot as plt
plt.style.use('grayscale')
from scipy.sparse import diags
import numpy as np

n = 4
# Différence finie d'ordre 1
# sous forme {\em forward}.
F = np.matrix(diags([1, -1], [0, 1], shape=(n,n)).toarray())
print(F)
#> [[ 1. -1.  0.  0.]
#>  [ 0.  1. -1.  0.]
#>  [ 0.  0.  1. -1.]
#>  [ 0.  0.  0.  1.]]

# Différence finie d'ordre 1
# sous forme {\em backward}.
B = np.matrix(diags([-1, 1], [0, 1], shape=(n,n)).toarray())
print(B)
#> [[-1.  1.  0.  0.]
#>  [ 0. -1.  1.  0.]
#>  [ 0.  0. -1.  1.]
#>  [ 0.  0.  0. -1.]]

# L'application de ces deux
# différentiations donne la matrice
# pour l'ordre 2.
print(F * B)
#> [[-1.  2. -1.  0.]
#>  [ 0. -1.  2. -1.]
#>  [ 0.  0. -1.  2.]
#>  [ 0.  0.  0. -1.]]

n = 90
h = 1 / n
A = np.matrix(diags([1, -2, 1], [-1, 0, 1], shape=(n,n)).toarray())
f = 1
F = np.array([f] * n)

# Conditions aux limites asymétriques.
F[0] += -15
F[n-1] += -25
Y = np.linalg.inv(A) * np.matrix(F).T

plt.scatter([-1, n], [15, 5])
plt.plot(Y)
plt.show()

# Vérification des conditions aux limites.
print('U0', f + 2 * Y[0] - Y[1])
print('UN+1', f + 2 * Y[n-1] - Y[n-2])
