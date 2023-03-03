# a est un entier
a = 12
print(type(a))
#> <class 'int'>

# x est un réel
x = 3.5
print(type(x))
#> <class 'float'>

# c est un booléen
c = True
print(type(c))
#> <class 'bool'>

# l est une liste
# les listes peuvent être hétérogènes
l = [1, 2, a, x, c]
print(type(l))
#> <class 'list'>

# A est un ensemble
# Contrairement à une liste, un ensemble garantit l'unicité
# des éléments en son sein
A = {1, 1, 2, 3, 4, 5, 6}
print(type(A))
#> <class 'set'>

# s est une chaîne de caractères
s = 'python'
print(type(s))
#> <class 'str'>

# D est un dictionnaire
D = {'key1' : 1, 'key2': 2, 'key3': 3}
print(type(D))
#> <class 'dict'>
