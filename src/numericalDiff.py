import numpy as np
from math import exp, sin, cos
import matplotlib.pyplot as plt

# Calcul de la dérivée selon une approche
# numérique, en repartant simplement de sa définition.
def numerical_diff(f, x, h=1e-3):
    return (f(x+h) - f(x)) / h


# Application au cas de l'exponentielle,
# dont la dérivée est elle-même !
x = 2
print(exp(2))
#> 7.38905609893065
print(numerical_diff(exp, 2))
#> 7.392751858796842
print(numerical_diff(exp, 2, h=1e-6))
#> 7.38905979424942
print(numerical_diff(exp, 2, h=0.1))
#> 7.771138136370013

# \'Etude de la réduction de l'erreur en fonction de $h$.
cube = lambda x : x**3
cube_derivative = lambda x : 3 * x**2
nb_points = 10000
H = np.linspace(0.1, 0.00001, nb_points)
Dsin = [numerical_diff(sin, 0, h=h) - cos(0) for h in H]
Dcube = [numerical_diff(cube, 0, h=h) - cube_derivative(0) for h in H]

plt.plot(range(0, nb_points), Dsin, '-.', label='Approximation de la derivee de sin(x)')
plt.plot(range(0, nb_points), Dcube, label='Approximation de la derivee de cube(x)')
plt.xlabel('h decroissant')
plt.legend()
plt.show()
