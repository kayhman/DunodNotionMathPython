import numpy as np
from sympy import symbols, expand, diff
from sympy.solvers import solve
import matplotlib.pyplot as plt

X = np.linspace(0, 5, 100)
p = lambda x: (x - 1 ) * (x - 3) * (x - 5)
Y = [p(x) for x in X]

# Nous créons une variable : x
x = symbols('x')

print(diff(expand((x - 1) * (x - 3) * (x - 5))))
#> 3*x**2 - 18*x + 23
root = solve(diff(expand((x - 1) * (x - 3) * (x - 5))))
root = [float(r) for r in root]
print(root)
# [1.8452994616207485, 4.1547005383792515]
plt.plot(X, Y, label="y = (x-1)(x-2)(x-3)")
plt.plot(X, [p(root[0])] * len(X), '-.', label="tangente maximum")
plt.plot(X, [p(root[1])] * len(X), ':', label="tangente minimum")
plt.legend()
plt.show()

# La variation au voisinage d'un extremum
# est faible.
delta = 1e-3
print(p(root[0] + delta) - p(root[0]))
#> -3.4631016152530947e-06

# Pour un point quelconque
# ce n'est pas le cas.
print(p(1 + delta) - p(1))
#> 0.007994000999999121

# En exprimant cette variation
# relativement à la variation de x
# l'effet est encore plus frappant.

print((p(root[0] + delta) - p(root[0])) / delta)
#> -0.0034631016152530947

# Pour un point quelconque
# ce n'est pas le cas.
print((p(1 + delta) - p(1))  / delta)
#> 7.994
