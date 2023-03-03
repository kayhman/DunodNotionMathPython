from math import pi, cos, sin

# Cette classe implémente une  rotation 3D
# selon un axe donné.
class Rotation3D:
    def __init__(self, alpha, axis):
        self.axis = axis
        self.alpha = -alpha if axis == "y" else alpha
        self.coeffs = [1,
                       0, cos(alpha),
                       0, sin(alpha), cos(alpha)]

    # Cette fonction échange les coordonnées
    # pour changer l'axe de rotation.
    def _swap(self, vec):
        if self.axis == "y":
            return[vec[1], vec[0], vec[2]]
        elif self.axis == "z":
            return[vec[2], vec[1], vec[0]]
        return vec

    # Le calcul effectif de la rotation est réalisé ici
    # Une inversion est réalisée en amont et en aval
    # dans le cas où l'axe de rotation n'est pas $\vec{x}$.
    def __mul__(self, vec):
        vec = self._swap(vec)
        x = self.coeffs[0] * vec[0] - self.coeffs[1] * vec[1] - self.coeffs[3] * vec[2]
        y = self.coeffs[1] * vec[0] + self.coeffs[2] * vec[1] - self.coeffs[4] * vec[2]
        z = self.coeffs[3] * vec[0] + self.coeffs[4] * vec[1] - self.coeffs[5] * vec[2]
        return self._swap([x, y, z])

# En tournant de $pi$ autour de $\vec{x}$
# le point $P=(0, 1, 0)$ devient $P_{pi}=(0, 0, 1)$.
R = Rotation3D(pi/2.0, 'x')
print(R * [0, 1, 0])
#> [0, 6.123233995736766e-17, 1.0]

# En tournant de $pi$ autour de $\vec{y}$
# le point $P=(0, 1, 0)$ reste invariant
# car il est sur l'axe de rotation.
R = Rotation3D(pi/2.0, 'y')
print(R * [0, 1, 0])
#> [0.0, 1, 0.0]

# En tournant de $pi$ autour de $\vec{x}$
# le point $P=(0, 1, 0)$ devient $P_{pi}=(1, 0, 0)$.
R = Rotation3D(pi/2.0, 'z')
print(R * [0, 1, 0])
#> [1.0, 6.123233995736766e-17, 0]
