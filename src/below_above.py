import numpy as np

# define the plane with a point and a normal vector
A = np.array([3, 0, 0])
n = np.array([1, 0, 0])

# define two points, one above, the other below the plane
Aa = np.array([4, 1, 1])
Ab = np.array([2, 1, 0])


def above(P, A, n):
    sign = (P - A).dot(n)
    return True if sign > 0 else False

print('Is Aa above:', above(Aa, A, n))
# -> Is Aa above: True
print('Is Ab above:', above(Ab, A, n))
# -> Is Aa above: False
