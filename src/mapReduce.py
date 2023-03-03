from functools import reduce

X = [x - 25 for x in range(0, 51)]
X2 = map(lambda x: x**2, X)
print(list(X2))
#> [625, 576, ...]

# Calcul de la fameuse somme
# des nombres de 1 à 100
# qu'a résolu Gauss très jeune.
X = [x for x in range(1, 101)]
sum = reduce(lambda x, y: x + y, X)
print(sum)
#> 5050


# Cas de la somme pondérée.
X = [x for x in range(1, 101)]
weights = [0 if x%2 == 0 else 1 for x in range(1, 101)]
sum = reduce(lambda x, y: x + y,
             map(lambda x: x[0] * x[1], zip(X, weights)))
print(sum)
#> 2500
