# Cette ligne ne va pas être comprise
# car elle commence par un espace.
# L'indentation est incorrecte
 variable_2 = 2
#> IndentationError: unexpected indent

# Cette boucle calcule la somme des nombres de 1 à 100
# de manière brute force, contrairement à ce qu'avait fait
# Gauss étant jeune étudiant
sum = 0
for i in range(1, 101):
    # ce bloc, identifié par l'indentation de 4 caractères
    # est exécuté autant de fois que la boucle l'impose
    sum += i

print(sum)
# > 5050

# Le corps d'une fonction se définit
# toujours dans un bloc en retrait
# d'une indentation
def gauss_sum():
    sum = 0
    for i in range(1, 101):
        # ce bloc, identifié par l'indentation de 4 caractères
        # est exécuté autant de fois que la boucle l'impose
        sum += i
    return sum
# le bloc de la fonction se termine ici

print(gauss_sum())
# > 5050
