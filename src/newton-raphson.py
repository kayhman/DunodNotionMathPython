# Caclule numériquement la dérivée de la fonction f au point x
# $f'(x) = \lim\limits_{d\rightarrow 0} \frac{f(x+d) - f(x)}{d}$.
def deriv(f, x, d=1e-3):
  return (f(x + d) - f(x)) / d


# Cherche une solution de f(x) = 0 au voisinage de $x_0$.
# $n$ est le nombre d'itérations.
def raphson(f, x0, n=5):
  xi = x0  # xi contient les approximations successives.
  for i in range(0, n):
    d = -f(xi) / deriv(f, xi)
    xi = xi + d
  return xi


f = lambda x: x**3 - 2 * x - 5
r = raphson(f, 2)
print(r)
#-> 2.09455148154233
print(f(r))
# -> 3.8191672047105385e-14
