def f(x):
    d = 0
    for c in x:
        d += c
    return d / len(x)

print(f([1, 2, 3, 4, 5]))
#> 3
