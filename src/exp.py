# compound\_interest calcule les intérêts composés
# pour un taux $r$
# un nombre de périodes $n$ sur l'année
# et une durée de $d$ ans.
def compound_interest(r, n, d):
    return (1 + r/n)**(n*d)

# Gain pour un placement d'une durée d'un an,
# à 5\%, avec calcul du gain une fois par an.
compound_interest(0.05, 1, 1)
# > 1.05

# Gain pour un placement d'une durée d'un an,
# à 5\%, avec évaluation des intérêts tous les mois.
compound_interest(0.05, 12, 1)
# > 1.051161897881733

# Que se passe-t-il lorsque n tend vers l'infini ?
compound_interest(1.0, 1, 1)
# > 2.0
compound_interest(1.0, 10, 1)
# > 2.5937424601000023
compound_interest(1.0, 100, 1)
# > 2.7048138294215285
compound_interest(1.0, 1000, 1)
# > 2.7169239322355936
compound_interest(1.0, 10000, 1)
# > 2.7181459268249255
compound_interest(1.0, 1000000, 1)
# > 2.7182804690957534


# Calcul de $e^x$ selon la méthode d'Euler.
def exp_euler(r, max_iter=20):
    # max pour ne pas dépasser la capacité des flottants.
    fact = 1
    res = 0.0
    r_n = 1
    for n in range (0,max_iter):
        # calcul de n! (factorielle(n)).
        fact = fact * 1 if n == 0 else n
        res +=  r_n / fact
        r_n = r * r_n # calcul de $x^n$.
    return res
