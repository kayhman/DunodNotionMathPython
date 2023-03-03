# Cette classe implémente le mécanisme de
# la différentiation automatique.
class AutoReal:
    # \`A l'initialisation deux champs sont remplis pour cet objet
    # sa valeur $val$ et sa dérivée $der$.
    def __init__(self, val, der):
        self.val = val
        self.der = der

    # L'addition suit la formule suivante:
    # $(u+v)' = u' + v'$
    def __add__(self, b):
        if isinstance(b, (float, int)):
            b = AutoReal(b, 0)
        return AutoReal(self.val + b.val, self.der + b.der)

    # La soustraction suit la formule suivante :
    # $(u-v)' = u' - v'$
    def __sub__(self, b):
        if isinstance(b, (float, int)):
            b = AutoReal(b, 0)
        return AutoReal(self.val - b.val, self.der - b.der)

    # La multiplication suit la formule suivante :
    # $(u*v)' = u' * v + u * v'$
    def __mul__(self, b):
        if isinstance(b, (float, int)):
            b = AutoReal(b, 0)
        return AutoReal(self.val * b.val, self.val * b.der + self.der * b.val)

    # La division suit la formule suivante :
    # $(\frac{u}{v})' = \frac{u' * v - u * v'}{v^2}$
    def __div__(self, b):
        if isinstance(b, (float, int)):
            b = AutoReal(b, 0)
        return AutoReal(self.val / b.val, (self.der * b.val - self.val * b.der) / (b.val * b.val))

    def __str__(self):
        return f'Valeur: {self.val}, Derivee: ({self.der})'


p = lambda x : (x - 1) * (x - 3) * (x - 5)
# La dérivée de ce polynôme, comme vu page \pageref{extremum} est :
p_prime = lambda x : 3*x**2 - 18*x + 23
x = AutoReal(3, 1)

# La dérivée en $x = 3$ va être calculée automatiquement,
# en même temps que la valeur :
print(p(x))
#> Valeur: 0, Derivee: (-4)
# Le résultat obtenu avec la formule est le même.
print(p_prime(3))
#> -4
