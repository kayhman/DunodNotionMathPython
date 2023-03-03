from math import exp, factorial
from sympy import integrate
import cProfile
import matplotlib.pyplot as plt

plt.style.use('grayscale')

# Implémentation simple de la factorielle.
def trivial_factorial(n):
    prod = 1
    for k in range(1, n+1):
        prod *= k
    return prod


print(trivial_factorial(3))
#> 6

print(trivial_factorial(20))
#> 2 432 902 008 176 640 000

# Calcul de la factorielle pour les 20 premiers entiers.
X = list(range(0, 20))
Y = [trivial_factorial(x) for x in X]

plt.scatter(X, Y, label='Factorielle')
plt.legend()
plt.show()


# Comparaison avec l'exponentielle.
E = [exp(x) for x in X]

plt.scatter(X, Y, label='Factorielle')
plt.plot(X, E, label='Exponentielle')
plt.legend()
plt.show()


# Implémentation récursive de la factorielle
# exploitant le fait que $n! = (n-1)!*n$.
def recursive_factorial(n):
    if n == 1:
        return 1
    return recursive_factorial(n-1) * n


print(recursive_factorial(20))

# Comparaison des temps d'exécution entre
# la fonction triviale et celle de Python.
cProfile.run('trivial_factorial(127000)')
#> 3.22 seconds
cProfile.run('factorial(127000)')
#> 0.192 seconds


# Taille en bits de l'entier généré.
# La limite de stockage d'un entier standard est rapidement atteinte.
r = factorial(20)
print(r.bit_length())
#> 62

r = factorial(126000)
print(r.bit_length())
#> 1953057


# Vérification de la généralisation de la factorielle
# aux réels avec la fonction $\Gamma$.
integrate(t**3 * exp(-t), t)
#> (-t**3 - 3*t**2 - 6*t - 6)*exp(-t)

-integrate(t**3 * exp(-t), t).subs({t:0})
#> 6
