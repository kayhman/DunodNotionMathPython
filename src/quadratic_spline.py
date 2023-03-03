from numpy import matrix, asarray, dot
import math
import random
from numpy.linalg import inv

import matplotlib.pyplot as plt

nbSamples = 30

X = [(x + 1) * 1.0 / nbSamples
               for x in range(nbSamples)]
Y = matrix([math.log(x)
               for x in X]).T

def Iplus(xi, x):
    return x - xi if x >= xi else 0.0

def splinify(xMin, xMax, step, x):
    a = [
        Iplus(xMin + i * step, x)
        for i in range(int((xMax - xMin) / step))
    ]
    a2 = [
        Iplus(xMin + i * step, x)**2
        for i in range(int((xMax - xMin) / step))
    ]
    a.reverse()
    a2.reverse()
    return a2 + a + [1]

Xsplines = matrix([
    splinify(0.0, 1.0, 1, x) for x in X
])

A = inv(Xsplines.T *
        Xsplines) * Xsplines.T * Y
YregLine = matrix([[dot(x, A).item(0)]
                      for x in Xsplines])

Xsplines = matrix([
    splinify(0.0, 1.0, 0.5, x)
    for x in X
])
print(Xsplines)

A = inv(Xsplines.T *
        Xsplines) * Xsplines.T * Y
YregCoarse = matrix([[dot(x, A).item(0)]
                        for x in Xsplines])

Xsplines = matrix([
    splinify(0.0, 1.0, 0.25, x)
    for x in X
])
print(Xsplines)
A = inv(Xsplines.T *
        Xsplines) * Xsplines.T * Y
Yreg = matrix([[dot(x, A).item(0)]
                  for x in Xsplines])

plt.style.use('grayscale')
plt.plot(X,
         asarray(Y),
         '+',
         label='Value to predict(log)')
plt.plot(X,
         YregLine,
         label='Linear regression')
plt.plot(X,
         YregCoarse,
         label='2 splines')
plt.plot(X,
         Yreg,
         label='20 splines')
plt.legend(loc="upper left")
plt.show()
