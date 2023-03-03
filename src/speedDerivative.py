# Calcul de la position à un instant t
# si le déplacement se fait à vitesse constante $V$.
def position(V, t):
    return V * t

# Fonction générique pour calculer la dérivée
# d'une fonction $f$ en un point $x$
# en prenant h suffisamment petit.
def derivative(f, x, h=1e-3):
    return (f(x+h) - f(x)) / h

# Calcul de la vitesse instantanée à un instant $t = 15$,
# pour une vitesse constante de 5.
print(derivative(lambda x : position(5, x), 15))
# > 4.9999999999954525
