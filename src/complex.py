from sympy import symbols, diff, solve
import numpy as np
from cmath import sqrt
import matplotlib.pyplot as plt
plt.style.use('grayscale')

# Définition des paramètres a, b et c
# et de la variable x.
x, a, b, c = symbols("x a b c")

# Définition du polynôme p.
p = a*x**2 + b*x + c

# Dérivation du polynôme p
# par rapport à x pour obtenir le minimum.
d = diff(p, x)

print(d)
#> 2ax + b

# Obtention de la valeur de x pour laquelle
# le polynôme atteint un minimum si a est positive
# et un maximum si a est négative.
min = solve(d, x)
print(min)
#> [-b/(2*a)

# Minimum atteint en $x = \frac{-b}{2a}$.
print(p.subs(x, min))
#> c - b**2/(4*a)


# Tracé d'un polynôme sans solution réelle
# n'ayant pas d'intersection avec l'axe des abscisses.
a, b, c = 1, 0, 5

X = np.linspace(-10, 10, 100)
Y1 = [a * x**2 + b * x + c for x in X]

# Tracé d'un polynôme sans solution réelle
# avec $a < 0$
# se trouvant donc sous l'axe des abscisses.
a, b, c = -1, 0, -5

Y2 = [a * x**2 + b * x + c for x in X]

plt.plot(X, Y1, label="P(x) avec a positif")
plt.plot(X, Y2, label="P(x) avec a negatif")
plt.legend()
plt.show()

# Calcul des racines pour un polynôme
# sans solutions réelles.
a, b, c = 1, 0, 5

delta = b**2 - 4 * a *c
print(delta)
#> - 10
x_1 = (-b + sqrt(delta)) / (2 * a)
x_2 = (-b - sqrt(delta)) / (2 * a)
print(x_1)
#> 2.23606797749979j
print(x_2)
#> -2.23606797749979j

# Vérification de la validité de la factorisation.
P = lambda x : a * x**2 + b * x + c
Pc = lambda x : (x - x_1) * (x - x_2)

# Le polynôme s'annule bien pour $x_1$.
print(P(x_1))
#> (-8.881784197001252e-16+0j)
print(Pc(x_1))
#> 0j

# Idem pour $x_2$.
print(P(x_2))
#> (-8.881784197001252e-16+0j)
print(Pc(x_2))
#> 0j


# Le minimum $c - \frac{b^2}{4a} = 5$ est atteint pour $x = \frac{-b}{2a}$.
print(P(-b / (2*a)))
#> 5
print(Pc(-b / (2*a)))
#> 5+0j
