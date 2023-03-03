import numpy as np

def dot(u, v):
    scalar = 0
    for ui, vi in zip(u, v):
        scalar += ui * vi
    return scalar

u = [1, 2, 3]
v = [4, 5, 6]
s = dot(u, v)
print(s)
#> 32

# Vérification avec la librairie
# numpy
print(np.dot(u, v))
#> 32


# Utilisation du produit scalaire
# pour déterminer la localisation
# d'un point par rapport à un plan

# Pour définir un plan
# il faut un point et
# un vecteur normal
A = np.array([3, 0, 0])

n = np.array([1, 1, 0])
# normalisation du vecteur
# pour que $\lVert \vec{n} \rVert = 1.0$
n = n / np.linalg.norm(n)
print(np.linalg.norm(n))
#> 0.99999999999

B = np.array([1, 1, 0])

# si B se trouve de l'autre côté
# du plan
# alors le cosinus de l'angle $\angle(\vec{AB}, \vec{n}) < 0$
AB = B - A
print(dot(AB, n))
#> -0.7071067811865475
# Le point B se situe bien
# de l'autre côté du plan.

# En le translatant sufissamment
# selon la normale, il repasse
# de l'autre côté
C = AB + 4 * n

# Le produit scalaire redevient positif
print(dot(C, n))
#> 3.2928932188134517
