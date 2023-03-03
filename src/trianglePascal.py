import numpy as np
from sympy import Symbol, expand


def pascalTriangle(depth):
    triangle = [[1]]
    for d in range(0, depth):
        layer = []
        prev_layer = [0] + triangle[-1] + [0]
        for i in range(0, len(prev_layer) - 1):
            layer += [prev_layer[i] + prev_layer[i+1]]
        triangle.append(layer)
    return triangle


def display(triangle):
    for line in triangle:
        print(line)


triangle = pascalTriangle(5)
display(triangle)
#> [1]
#> [1, 1]
#> [1, 2, 1]
#> [1, 3, 3, 1]
#> [1, 4, 6, 4, 1]
#> [1, 5, 10, 10, 5, 1]


x = Symbol("x")
y = Symbol("y")

# Développement d'un binôme à la puissance 4.
print(expand((x + y)**3))
#> $x^3 + 3*x^2*y + 3*x*y^2 + y^3$

print(expand((x + y)**4))
#> $x^4 + 4*x^3*y + 6*x^2*y^2 + 4*x*y^3 + y^4$

print(expand((x + y)**5))
#> $x^5 + 5*x^4*y + 10*x^3*y*^2 + 10*x^2*y^3 + 5*x*y^4 + y^5$

print(11**2)
#> 121

print(11**3)
#> 1331

print(11**4)
#> 14641
