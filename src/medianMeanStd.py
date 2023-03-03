import math
import numpy as np

# Calcul de la cardinalité
# soit simplement le nombre d'éléments d'un tableau.
def cardinality(data):
    return len(data)

# Calcul de la moyenne.
def mean(data):
    sum = 0
    for d in data:
        sum += d
    n = cardinality(data)
    return sum / n

# Calcul de l'écart-type.
def std(data):
    m = mean(data)
    n = cardinality(data)
    std = 0
    for d in data:
        std += (d - m)**2 / n
    return math.sqrt(std)

# Calcul de la médiane.
def median(data):
    n = cardinality(data)
    data = sorted(data)
    if n % 2 == 1: # n est impair.
        return data[n // 2]
    else:
        return (data[n // 2  - 1] + data[n // 2]) / 2

# Comparaison des fonctions définies ci-dessus
# avec les implémentations standard de numpy.
data = [1, 2, 3, 4, 5, 6]
print(cardinality(data))
print(mean(data), np.mean(data))
print(std(data), np.std(data))
print(median(data), np.median(data))
#> 6
#> 3.5 3.5
# > 1.7078251276599332 1.707825127659933
#> 3.5 3.5

# Ce nouvel ensemble de données
# a la même moyenne
# mais un écart-type nul.
data = [3.5, 3.5, 3.5, 3.5, 3.5, 3.5]
print(cardinality(data))
print(mean(data), np.mean(data))
print(std(data), np.std(data))
print(median(data), np.median(data))
#> 6
#> 3.5 3.5
#> 0.0 0.0
#> 3.5 3.5

# Ce nouvel ensemble de données
# a la même moyenne
# mais cette fois-ci une médiane
# différente
data = [0, 0, 0, 0, 0, 21]
print(cardinality(data))
print(mean(data), np.mean(data))
print(std(data), np.std(data))
print(median(data), np.median(data))
#> 6
#> 3.5 3.5
#> 7.826237921249264 7.826237921249264
#> 0.0 0.0
