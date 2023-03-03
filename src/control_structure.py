import random

# la condition est le résultat d'un test,
# c'est-à-dire que c'est un objet qui peut être interprété
# comme un booleen. Deux valeurs sont donc possibles : vrai ou faux
condition = True

# La structure de contrôle de base en Python
# prend la forme suivante
if condition:
    # alors on exécute le code dans le bloc qui suit
    print("la condition est vraie")
#> la condition est vraie

# Il est aussi possible d'avoir une alternative
# dans le cas où la condition serait fausse.
# C'est ce que permet le mot-clef else
if condition:
    # alors on exécute le code dans le bloc qui suit
    print("la condition est vraie")
else:
    # sinon ce bloc s'exécute
    print("la condition est fausse")
#> la condition est vraie

# Il est possible de mettre le code de la condition
# directement sur la ligne du if
x = random.random()
if x < 0.5:
    # alors on exécute le code dans le bloc qui suit
    print(f"{x} est strictement inferieur a 0.5")
else:
    # sinon ce bloc s'exécute
    print(f"{x} est superieur a 0.5")
#> résultat suivant la valeur de x


#Il est aussi possible d'enchaîner plusieurs tests avec {\em elif}
if x < 0.5:
    # alors on exécute le code dans le bloc qui suit
    print(f"{x} est strictement inferieur a 0.5")
elif x < 0.6:
    print(f"{x} est entre 0.5 et 0.6")
else:
    # sinon ce bloc s'exécute
    print(f"{x} est superieur a 0.5")
#> résultat suivant la valeur de x
