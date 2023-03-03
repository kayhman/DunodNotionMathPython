import matplotlib.pyplot as plt
plt.style.use('grayscale')
import numpy as np


# Fonction calculant
# la série de termes u(k)
def serie(u, n, start=0):
    return np.sum([u(k) for k in range(start, n)])


# Application à la série
# $S_k = \sum_{k=0}^n \left(\frac{1}{2}\right)^k$
N = 40
X = [n for n in range(0, N)]
Y = [serie(lambda k : (1/2)**k, n) for n in X]
# Dernier terme de la série
print(Y[-1])
# > 1.999999999996362
plt.plot(X, Y, label='Somme des (1/2)**k pour k dans [0, n]')
plt.legend()
plt.show()


# Application à la série
# $S_n = \sum_{k=1}^n \left(\frac{1}{k}\right)$
N = 1000
X = [n for n in range(1, N)]
Y = [serie(lambda k : (1/k), n, 1) for n in X]
# Dernier terme de la série
print(Y[-1])
# > 7.483469859549345
plt.plot(X, Y, label='Somme des 1/k pour k dans [0, n]')
plt.legend()
plt.show()
