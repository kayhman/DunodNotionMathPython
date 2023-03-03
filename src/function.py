# La fonction identité se retrouve souvent en mathématique.
# Par exemple pour tester une idée mathématique
# ou un concept dans le cas le plus simple.
def identity(x):
    return x
from functools import reduce

# La fonction carré est aussi très présente.
# Cela découle de son importance en physique
# où elle intervient régulièrement dans le calcul
# d'énergie.
def square(x):
    return x * x

# Exemple de la fonction inverse
# dont le domaine de définition est $\mathbb{R} \setminus 0$
# soit l'ensemble des réels sans 0.
def inverse(x):
    return 1/x

# Les fonctions polynôme sont une monnaie courante.
def polynome(A, x):
    return reduce(lambda a, b: a + b,
                  [a_i * x**i for i, a_i in enumerate(A)], 0)

print(identity(6))
#> 6
print(square(6))
#> 36
print(inverse(2))
#> 0.5

# L'inverse de 0 n'est pas calculable
# Python lève une exception.
#print(inverse(0))
#> ZeroDivisionError: division by zero
print(polynome([1, 2, 3], 1))
#> 6

# Définition itérative de la fonction puissance.
# $f : x \rightarrow x^n$
def iterative_power(x, n):
    #utilisation d'une variable power
    power = 1
    for i in range(0, n):
        power = power * x
    return power

# Définition fonctionnelle de la fonction puissance.
# $f : x \rightarrow x^n$
def fonctional_power(x, n):
    return x * fonctional_power(x, n-1) if n != 1 else 1

print(iterative_power(2, 4))
#> 16
print(iterative_power(2, 4))
#> 16
