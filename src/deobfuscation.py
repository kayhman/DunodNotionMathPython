def mean(xs):
    """
    Cette fonction calcule la somme
    des elements du tableau xs.
    """
    sum = 0
    for x in xs:
        sum += x
    return sum / len(xs)

print(mean([1, 2, 3, 4, 5]))
#> 3
