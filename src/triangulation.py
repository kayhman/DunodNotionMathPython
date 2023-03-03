import matplotlib.pyplot as plt
plt.style.use('grayscale')
import numpy as np
import random

random.seed(42)

# Génération d'un nuage de points aléatoires
points = [(random.random() - 0.5, random.random() - 0.5) for i in range(0, 100)]
points = sorted(points, key=lambda p: p[0])
print(points)

class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def to_plot(self):
        return np.array([self.a, self.b, self.c])

triangles = [Triangle(points[0], points[1], points[2])]

for idx, pnt in enumerate(points[3:]):
    pm2 = points[2 + idx - 2]
    pm1 = points[2 + idx - 1]
    triangles.append(Triangle(pm2, pm1, pnt))

print(len(triangles))

plt.figure()
plt.scatter([p[0] for p in points], [p[1] for p in points])
for triangle in triangles[0:2]:
    trg = plt.Polygon(triangle.to_plot())
    plt.gca().add_patch(trg)
plt.show()
