import numpy as np

# define the plane with a point and a normal vector
A = np.array([3, 0, 0])
n = np.array([1, 0, 0])

# define two points, one above, the other below the plane
Aa = np.array([4, 1, 1])
Ab = np.array([2, 1, 0])

def project(P, A, n):
    P = P - ((P - A).dot(n)) * n
    return P


print('Aa projection is:', project(Aa, A, n))
# -> Aa projection is: [3 1 1]
print('Ab projection is:', project(Ab, A, n))
# -> Ab projection is: [3 1 0]
