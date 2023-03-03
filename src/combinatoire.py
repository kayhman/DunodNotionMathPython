from itertools import permutations, combinations, product

data = ['A', 'B', 'C', 'D']

# Calcul de toutes les permutations
# possibles pour la liste data.
for p in permutations(data):
    print(p)
#> ('A', 'B', 'C', 'D')
#> ('A', 'B', 'D', 'C')
#> ('A', 'C', 'B', 'D')
#> ('A', 'C', 'D', 'B')
#> ('A', 'D', 'B', 'C')
#> ('A', 'D', 'C', 'B')
#> ('B', 'A', 'C', 'D')
#> ('B', 'A', 'D', 'C')
#> ('B', 'C', 'A', 'D')
#> ('B', 'C', 'D', 'A')
#> ('B', 'D', 'A', 'C')
#> ('B', 'D', 'C', 'A')
#> ('C', 'A', 'B', 'D')
#> ('C', 'A', 'D', 'B')
#> ('C', 'B', 'A', 'D')
#> ('C', 'B', 'D', 'A')
#> ('C', 'D', 'A', 'B')
#> ('C', 'D', 'B', 'A')
#> ('D', 'A', 'B', 'C')
#> ('D', 'A', 'C', 'B')
#> ('D', 'B', 'A', 'C')
#> ('D', 'B', 'C', 'A')
#> ('D', 'C', 'A', 'B')
#> ('D', 'C', 'B', 'A')


# Calcul de toutes les combinaisons possibles
# pour 2 éléments de la liste data.
for c in combinations(data, 2):
    print(c)
#> ('A', 'B')
#> ('A', 'C')
#> ('A', 'D')
#> ('B', 'C')
#> ('B', 'D')
#> ('C', 'D')


# Calcul de tous les arrangements possibles
# pour 2 éléments de la liste data.
for c in product(data, repeat=2):
    print(c)
#> ('A', 'B')
#> ('A', 'C')
#> ('A', 'D')
#> ('B', 'C')
#> ('B', 'D')
#> ('C', 'D')
#> ('A', 'A')
#> ('A', 'B')
#> ('A', 'C')
#> ('A', 'D')
#> ('B', 'A')
#> ('B', 'B')
#> ('B', 'C')
#> ('B', 'D')
#> ('C', 'A')
#> ('C', 'B')
#> ('C', 'C')
#> ('C', 'D')
#> ('D', 'A')
#> ('D', 'B')
#> ('D', 'C')
#> ('D', 'D')
