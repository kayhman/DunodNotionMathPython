# Python supporte nativement les ensembles
# Deux syntaxes sont possibles pour les définir :
A = {1, 2, 3, 4, 5, 6}
B = set(['A', 'B', 'C', 'D'])

# union $A \cup  B$
print(A.union(B))
#> {1, 2, 3, 4, 5, 6, 'D', 'A', 'C', 'B'}

# intersection $A \cap B$
print(A.intersection(B))
#> set()

# intersection $A - B$
print(A.difference(B))
#> set({1, 2, 3, 4, 5, 6})

# inclusion $A \in B$
print(A.issubset(B))
#> False

# inclusion ${1, 2} \in A$
print({1, 2}.issubset(A))
#> True

# inclusion $A = B$
print(A == B)
#> False

# inclusion ${1, 2, 3, 4, 5, 6} = A$
print({1, 2, 3, 4, 5, 6} == A)
#> True

# Python supporte aussi la définition d'ensemble sous forme de compréhension
# ici un exemple regroupant les nombres pairs entre 0 et 11
print({x for x in range(0, 12) if x % 2 == 0})
#> {0, 2, 4, 6, 8, 10}
