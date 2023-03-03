import numpy as np

# Implémentation de la somme
def sum(data):
    sum = 0
    for d in data:
        sum += d
    return sum

# Implémentation du produit
def product(data):
    prod = 1
    for d in data:
        prod *= d
    return prod

data = range(1, 101)
print(list(data))

print(sum(data))
#> 5050
data = [1, 2, 3, 4, 5]
print(product(data))
#> 120
