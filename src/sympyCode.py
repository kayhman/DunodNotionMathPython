from sympy import symbols, expand, diff

x, a, b, c = symbols('x a b c')

p = a*x**2 + b * x + c
print(p)
#> a*x**2 + b*x + c

# Sympy supporte la dérivation.
# Ici par rapport à $x$.
print(diff(p, x))
#> 2*a*x + b

# Dérivation par rapport à $a$.
print(diff(p, a))
#> x**2

# Sympy sait aussi développer des expressions.
expand(p * p)
#> a**2*x**4 + 2*a*b*x**3 + 2*a*c*x**2 + b**2*x**2 + 2*b*c*x + c**2
