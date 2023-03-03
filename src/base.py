# Retourne la liste des chiffres composant un entier.
# Ex. : digits(123) -> [3, 2, 1]
def digits(n):
    return [int(c) for c in reversed(str(n))]

# from\_base convertit un entier n encodé en base b
# vers la base 10.
def from_base(n, b):
    value = 0
    for (idx, digit) in enumerate(digits(n)):
        # idx: la position du chiffre
        # d: ce chiffre
        value += digit * b**idx
    return value

# Calcule la valeur en base 8 de 12.
from_base(12, 8)
# -> $10 = 1 * 8^1 + 2 * 8^0$

# Calcule la valeur en base 8 de 12.
from_base(1234, 8)
# -> $668 = 1 * 8^3 + 2 * 8^2 + 3 * 8^1 + 4 * 8^0$


# to\_base convertit un entier n encodé en base 10
# vers la base b.
def to_base(n, b):
    digits = [] # contiendra la liste des chiffres, en ordre inverse.
    while n > b:
        digit = n % b
        n = n // b
        digits.append(digit)
    digits.append(n)
    value = 0
    # Nous inversons et parcourons la liste des chiffres.
    for digit in reversed(digits):
        value = 10 * value + digit
    return value


# Convertit 10 en base 10 vers la base 8.
to_base(10, 8)
# -> $12$ Nous retrouvons bien la valeur obtenue avec {\em from\_base}.

# Vérifions que la combinaison de from\_base et to\_base est l'identité.
identity = lambda n, b: from_base(to_base(n, b), b)
identity(12, 8)
# -> $12$ {\em identity} a bien laissé 12 invariant.

# Même vérification, mais en inversant l'ordre des opérations.
# Nous n'avons pas le choix de la base, n étant forcément exprimé en base 10.
identity = lambda n: to_base(from_base(n, 10), 10)
identity(12)
# -> $12$ {\em identity} a bien laissé 12 invariant.
