import matplotlib.pyplot as plt
plt.style.use('grayscale')
import numpy as np

# Définition des 3 points du triangle.
A = np.array([0, 0])
B = np.array([3, 0])
C = np.array([0, 4])

# Le point P se trouve dans du triangle.
P = np.array([2, 1])

# Le point P2 se trouve hors du triangle.
P2 = np.array([2, 2])

# Calcul de la surface du triangle ABC
sABC = np.linalg.det(np.matrix([B - A, C - A]))

def barycentric_coordinates(A, B, C, P):
    # Calcul de la surface des triangles
    # PBC, APC et ABP.
    sPBC = np.linalg.det(np.matrix([B - P, C - P]))
    sAPC = np.linalg.det(np.matrix([C - P, A - P]))
    sABP = np.linalg.det(np.matrix([A - P, B - P]))

    # Les coordonnées barycentriques
    # sont les ratios entre les surfaces
    # des petits triangles et du grand
    a = sPBC / sABC
    b = sAPC / sABC
    c = sABP / sABC
    return a, b, c
a, b, c = barycentric_coordinates(A, B,
                                  C, P)
print(a, b, c)
#> 0.08333333333333333 0.6666666666666665 0.24999999999999997

# La relation $\sum \lambda_i\vec{BP_i} = \vec{0}$
# est bien respectée.
Pb = a * (A - P) + b * (B - P) + c * (C - P)
print(Pb)
#> [-5.55111512e-17  0.00000000e+00]

# Même chose pour le point $P_2$.
a, b, c = barycentric_coordinates(A, B, C, P2)
# l'une des coordonnées est négative
# le point se trouve à l'extérieur
# du triangle.
print(a, b, c)
#> -0.16666666666666666 0.6666666666666665 0.5


# Tracé du triangle
# et des points intérieurs et extérieurs.
points = [A, B, C]
trg = plt.Polygon(points)
plt.gca().add_patch(trg)
plt.scatter([pts[0] for pts in points], [pts[1] for pts in points])
plt.scatter([pts[0] for pts in [P]], [pts[1] for pts in [P]])
plt.scatter([pts[0] for pts in [P2]], [pts[1] for pts in [P2]])
plt.annotate('P', P)
plt.annotate('P2', P2)
plt.show()
