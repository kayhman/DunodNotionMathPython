from sympy import symbols, expand, factor, solve, simplify, core
from skimage import io
import numpy as np

a, dx, dy, dz = symbols('a dx dy dz')
x, y, z = symbols('x y z')
cx, cy, cz, r = symbols('cx cy cz r')

sphere = (cx - x)**2 + (cy - y)**2 + (cz - z)**2 - r**2
ray_x, ray_y, ray_z = a * dx, a * dy, a * dz

sol = solve(sphere.subs(x, ray_x).subs(y, ray_y).subs(z, ray_z), a)
# solution générale du problème de l'intersection.
print(sol[0])

class Sphere:
    def __init__(self, C, radius):
        self.C = np.array(C)
        self.radius = radius
        a, dx, dy, dz = symbols('a dx dy dz')
        x, y, z = symbols('x y z')

        sphere = (C[0] - x)**2 + (C[1] - y)**2 + (C[2] - z)**2 - radius**2
        ray_x = a * dx
        ray_y = a * dy
        ray_z = a * dz

        self.sol = solve(sphere.subs([(x, ray_x), (y, ray_y), (z, ray_z)]), a)

    def intersect(self, ray):
        # Le polynôme étant d'ordre deux
        # deux solutions sont possibles.
        sol0 = self.sol[0].xreplace({dx: ray[0],
                                 dy: ray[1],
                                 dz: ray[2]})
        sol1 = self.sol[1].xreplace({dx: ray[0],
                                     dy: ray[1],
                                     dz: ray[2]})
        # Parmi celles réelles, seule la plus proche
        # est conservée.
        return min([sol for sol in [sol0, sol1] if isinstance(sol, core.numbers.Float) and sol > 0] or [-1])


sphere = Sphere([0, 0, 2], 0.7)
inter = sphere.intersect([0, 0, 1])
# L'intersection se trouve bien en alpha  = 1.3,
# soit $P = (0, 0, 1.3)$.
print(inter)

def render(objects, dims, sun):
    img = np.zeros(dims)
    for i in range(0, dims[0]):
        print('handle line', i,)
        for j in range(0, dims[1]):
            ray = np.array([(i - dims[0] / 2.0) / dims[0], (j - dims[1] / 2.0) / dims[1], 1])
            ray = ray / np.linalg.norm(ray)
            for obj in objects:
                inter = obj.intersect(ray)
                if  inter > 0:
                    x = ray * float(inter)
                    n = x - obj.C
                    n = n / np.linalg.norm(n)
                    l = sun - x
                    l = l / np.linalg.norm(n)
                    img[i, j] = n.dot(l) * 255
    return img

img = render([sphere], (1024, 1024), np.array([0, 3, 0]))
io.imsave('sphere.png', img)
