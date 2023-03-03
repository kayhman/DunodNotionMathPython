from numpy import matrix, asarray, dot
import math
import random
from numpy.linalg import inv

import matplotlib.pyplot as plt

nbSamples = 30

X = [(x + 1)/ nbSamples for x in range(nbSamples)]
Y = matrix([math.log(x) for x in X]).T

def Iplus(xi, x):
    return x - xi if x >= xi else 0.0

def splinify(xMin, xMax, step, x):
    a = [Iplus(xMin + i * step, x)
         for i in reversed(range(int((xMax - xMin) / step)))]
    return a + [1]

def least_square_fitting(X, Y):
    X = matrix(X)
    return inv(X.T * X) * X.T * Y

Xsplines = [splinify(0.0, 1.0, 1, x) for x in X]

A = least_square_fitting(Xsplines, Y)
YregLine = [dot(x, A).item(0) for x in Xsplines]

Xsplines = [splinify(0.0, 1.0, 0.25, x) for x in X]

A = least_square_fitting(Xsplines, Y)
plt.style.use('grayscale')
plt.plot(X, asarray(Y), '+', label='\'Echantillons du logarithme')

for poly_id in reversed(range(0, A.shape[0])):
    Aa = A.copy()
    for row in range(0, A.shape[0]):
        if row != poly_id:
            Aa[row, 0] = 0
    spline_i = [dot(x, Aa).item(0) for x in Xsplines]
    plt.plot(X,
             spline_i,
             label=f'Contribution du polynome {A.shape[0] - poly_id - 1}')

plt.legend(loc="upper left")
plt.show()

plt.plot(X, asarray(Y), '+', label='\'Echantillons du logarithme')
for poly_id in reversed(range(0, A.shape[0])):
    Aa = A.copy()
    for row in range(0, A.shape[0]):
        if row < poly_id:
            Aa[row, 0] = 0
    spline_i = [dot(x, Aa).item(0) for x in Xsplines]
    plt.plot(X,
             spline_i,
             label=f'Combinaison de {A.shape[0] - poly_id - 1} polynome(s)')

plt.legend(loc="upper left")
plt.show()
