import matplotlib.pyplot as plt
plt.style.use('grayscale')
import numpy as np
import random

# Génération d'un nuage de points aléatoires.
points = [(random.random() - 0.5, random.random() - 0.5) for i in range(0, 100)]


# Construction des kdtrees
def build_kdtree(pts, axis):
    if len(pts) <= 10:
        return []
    split = []
    # Les points sont séparés en deux selon la médiane.
    median = np.median([p[axis] for p in pts])
    left = [p for p in pts if p[axis] <= median]
    right = [p for p in pts if p[axis] >= median]

    split += [(axis,
               max(left, key=lambda p: p[axis]),
               min(pts, key=lambda p: p[(axis+1)%2]),
               max(pts, key=lambda p: p[(axis+1)%2]))]
    # Le même algorithme est appliqué récursivement
    # aux deux ensembles de points générés.
    split += build_kdtree(left, (axis+1)%2)
    split += build_kdtree(right, (axis+1)%2)
    return split

splits = build_kdtree(points, 0)
print(splits)


plt.scatter([p[0] for p in points], [p[1] for p in points])
for split in splits:
    axis, median, pmin, pmax = split
    if axis == 0:
        plt.plot([median[axis]] * 100, np.linspace(pmin[1], pmax[1], 100))
    else:
       plt.plot(np.linspace(pmin[0], pmax[0], 100), [median[axis]] * 100)
plt.show()
