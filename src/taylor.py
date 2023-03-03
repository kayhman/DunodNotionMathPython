from math import factorial, sqrt
import matplotlib.pyplot as plt
plt.style.use('grayscale')
import numpy as np
import sympy

# Test de l'expansion en série de Taylor
# pour $f(x) = x^2$.
f = lambda x : x**2
fp = lambda x : 2*x
fpp = lambda x : 2


x_0 = 2
taylor_f = lambda h : f(x_0) + fp(x_0) * h + fpp(x_0) * h**2/2

print(f(2 + 0.3))
#> 5.29
print(taylor_f(0.3))
#> 5.29

# Test de l'expansion en série de Taylor
# pour $f(x) = \sqrt{x}$.
# à l'ordre 3
f = lambda x : sqrt(x)
fp = lambda x : 1 / (2*sqrt(x))
fpp = lambda x : -1 / (4 * x * sqrt(x))
fppp = lambda x : (3 * sqrt(x)) / (8 * x**3)

taylor_f = lambda h : f(x_0) + fp(x_0) * h + fpp(x_0) * h**2/2 + fppp(x_0) * h**3/factorial(3)

print(f(2 + 0.3))
#> 1.51657508881031
print(taylor_f(0.3))
#> 1.5166004145802159

# Ajout d'un terme
# pour voir le gain en précision.
fpppp = lambda x : -15/(16*x**(7/2))
taylor_f = lambda h : f(x_0) + fp(x_0) * h + fpp(x_0) * h**2/2 + fppp(x_0) * h**3/factorial(3) + fpppp(x_0) * h**4/factorial(4)

# De manière approximative
# ajouter un ordre fait gagner
# une décimale.
print(taylor_f(0.3))
#> 1.5165724479545928

taylor_f = lambda h : f(x_0) + fp(x_0) * h + fpp(x_0) * h**2/2 + fppp(x_0) * h**3/factorial(3)
X = np.linspace(0, 4, 100)
Y = [f(x) for x in X]
taylor_Y = [taylor_f(x-2) for x in X]

plt.plot(X, Y, label='sqrt(x)')
plt.plot(X, taylor_Y, '-.', label='Expansion de Taylor de sqrt(x)')
plt.legend()
plt.show()
