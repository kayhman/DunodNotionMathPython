# Construction d'une liste d'abscisse.
X = [x - 25 for x in range(0, 51)]
print(X)
#> [-25, -24, ..., 24, 25]

# Y contient les valeurs absolues
# des éléments de X.
Y = [x if  x > 0 else -x for x in X]
print(Y)
#> [25, 24, ..., 24, 25]

# Les comprehension lists peuvent aussi être utilisées pour filtrer.
# Z ne contient que les éléments positifs ou nuls de X.
Z = [x for x in X if x >= 0]
print(len(Z))
#> 26
print(Z)
#> [1, 2, 3, ..., 24, 25]


# Le même mécanisme est disponible pour des dictionnaires.
tmp = {'key1' : 1, 'key2' : 2, 'key3' : 3}
dct = {key: val for key, val in tmp.items()}
print(dct)
#> {'key1': 1, 'key2': 2, 'key3': 3}

# Le filtrage est aussi possible sur les dictionnaires.
dct = {key: val for key, val in tmp.items() if val > 2}
print(dct)
#> {'key1': 1, 'key2': 2, 'key3': 3}
