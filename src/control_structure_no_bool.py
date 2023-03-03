import random

# La condition est ici une liste vide.
# Elle est considérée comme fausse
condition = []

if not condition:
    print("la condition est vraie")
else:
    print("la condition n'est pas vraie")
#> la condition n'est pas vraie

# Ici, la condition contient un élément
# Elle est considérée comme vraie
condition = {1}

if not condition:
    print("la condition est vraie")
else:
    print("la condition n'est pas vraie")
#> la condition n'est pas vraie
