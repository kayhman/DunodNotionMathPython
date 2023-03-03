from functools import reduce
from timeit import timeit

# Implémentation naïve d'une fonction polynôme.
def polynomial(A, x):
    return reduce(lambda a, b: a + b,
                  [a_i * x**i for i, a_i in enumerate(A)], 0)

# Implémentation économe en calculs
# d'une fonction polynôme.
def smarter_polynomial(A, x):
    p = A[0]
    for i in range(1, len(A)):
        p += A[i] * x
        x *=  x
    return p


A = [1, 2, 3]
print(polynomial(A, 2))
# > 17
print(smarter_polynomial(A, 2))
# > 17

def test_naive(n):
    for i in range(0, n):
        polynomial(A, 3)

def test_smarter(n):
    for i in range(0, n):
        smarter_polynomial(A, 3)

print(timeit("test_naive(10)", globals=locals()))
#> 16.60 s
print(timeit("test_smarter(10)", globals=locals()))
#> 6.04 s
