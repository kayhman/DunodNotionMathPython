from sympy import symbols, factor, re, im, simplify
import matplotlib.pyplot as plt
from math import sqrt, atan2

# \`A l'aide de sympy,
# les symboles ra, rb, ia et ib
# sont définis.
ra, rb = symbols('ra rb', real=True)
ia, ib = symbols('ia ib', imaginary=True)

a = ra + ia
b = rb + ib

# sympy supporte aussi le calcul symbolique
# avec les nombres complexes.
print(simplify(re(a * b)))
#> ia*ib + ra*rb
print(simplify(im(a * b)))
#> (ia*rb + ib*ra)

# Calcul de la représentation polaire
# des complexes.
c =  0.5 + 0.5j
# calcul du rayon r
r = sqrt(c.imag**2 + c.real**2)
# et de l'angle theta.
theta = atan2(c.imag, c.real)
print(r)
#> 0.7071067811865476
print(theta)
#> 0.7853981633974483

# Affichage en mode polaire avec
# matplotlib.
plt.axes(projection = 'polar')
plt.polar(theta, r, 'k.', markersize=40)
plt.show()

# En multipliant c par lui-même
# son rayon va être multiplié par r
# et son angle doublé.
c2  = c * c
r2 = sqrt(c2.imag**2 + c2.real**2)
theta2 = atan2(c2.imag, c2.real)
plt.axes(projection = 'polar')
plt.polar(theta, r, 'k.', markersize=40, label='c')
plt.polar(theta2, r2, 'k.', markersize=40, label='c*c')
plt.show()
