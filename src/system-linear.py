# Les variables $a, b, c$ et $p$ sont
# respectivement l'âge des 3 enfants et du père.

# Chacune des fonctions ci-dessous représentent
# les contraintes du problème.
l1 = lambda a,b,c,p: 2 * a + b + c - p
l2 = lambda a,b,c,p: 1.5 * b - c
l3 = lambda a,b,c,p: 3 * c - p - 2
l4 = lambda a,b,c,p: p - 43

# \`A l'aide de la définition des lignes $l_i$ du système,
# qui doivent être égales à 0,
# il est possible de calculer $a, b, c$ et $p$.
calc_a = lambda a,b,c,p: -1/2 * l1(0,b,c,p)
calc_b = lambda a,b,c,p: -1/1.5 * l2(a,0,c,p)
calc_c = lambda a,b,c,p: -1/3 * l3(a,b,0,p)
calc_p = lambda a,b,c,p: -l4(a,b,c,0)

# La solution est calculée de manière itérative.
def solution(a,b,c,p, n):
    for i in range(0,n):
        a = calc_a(a,b,c,p)
        b = calc_b(a,b,c,p)
        c = calc_c(a,b,c,p)
        p = calc_p(a,b,c,p)
    return a,b,c,p


print(solution(8,8,8,35, 1))
# -> (9.5,5.333,12.333,43)
print(solution(8,8,8,35, 2))
# -> (12.668,8.221,15.0,43)
print(solution(8,8,8,35, 3))
# -> (9.889,10.0,15.0,43)
print(solution(8,8,8,35, 4))
# -> (9.0,10.0,15.0,43)

a, b, c, p = solution(8,8,8,35, 4)
# Il est possible de vérifier le respect des contraintes du système
# à l'aide des fonctions $l_i$, dont le résultat doit être zéro.
print(l1(a, b, c, p))
# > 0.0
print(l2(a, b, c, p))
# > 0.0
print(l3(a, b, c, p))
# > 0.0
print(l4(a, b, c, p))
# > 0
