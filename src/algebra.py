from sympy import symbols, expand, factor
# Nous créons trois variables : t, x et y.
t, x, y = symbols('t x y')

# Ici, nous allons appliquer les règles du calcul algébrique pour simplifier
# l'expression $t^2 + t * (t + t^3)$.
print(expand(t**2 + t * (t + t**3)))
# > $t^4 + 2(t^2)$
print(factor(t**2 + t * (t + t**3)))
# > $t^2*(t^2 + 2)$
