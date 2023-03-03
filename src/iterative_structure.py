# La forme la plus classique d'une boucle d'itération est la suivante :
# il s'agit de répéter $n$ fois le même bloc de code.
n = 5
for i in range(0, n):
    print(i)
#> 0
#> 1
#> 2
#> 3
#> 4

# L'utilisation de {\em while} permet d'arriver au même résultat
# avec cependant une formulation un peu moins lisible.
i = 0
while i < 5:
    print(i)
    i += 1
#> 0
#> 1
#> 2
#> 3
#> 4

# Le Python permet d'itérer directement sur
# des structures de données itérables
# comme les listes.
data = [0, 1, 2, 3, 4]
for i in data:
    print(i)
#> 0
#> 1
#> 2
#> 3
#> 4

# Le mot-clef {\em continue} permet de sauter
# directement à l'itération suivante.
# Dans l'exemple suivant, il est utilisé
# pour n'afficher que les nombres pairs.
for i in range(0, 5):
    if i % 2 == 1:
        # pour les nombres impairs, la boucle s'arrête ici
        continue
    print(i)
#> 0
#> 2
#> 4

# Le mot-clef {\em break} permet quant à lui
# d'interrompre complètement une boucle.
# Ci-dessus, on recherche un nombre dans un tableau
# une fois celui-ci trouvé, la boucle s'arrête.
data = [6, 2, 1, 3, 0, 4, 5]
for d in data:
    if d == 0:
        print("found 0")
        break
# > found 0
