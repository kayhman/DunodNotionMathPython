import matplotlib.pyplot as plt
plt.style.use('grayscale')
import numpy as np
import random
random.seed(2)


X0 = [random.gauss(1, 0.3) for i in range(0, 50)]
Y0 = [random.gauss(1, 0.3) for i in range(0, 50)]

X1 = [random.gauss(4, 0.2) for i in range(0, 50)]
Y1 = [random.gauss(2, 0.2) for i in range(0, 50)]

X2 = [random.gauss(-3, 0.4) for i in range(0, 50)]
Y2 = [random.gauss(3, 0.4) for i in range(0, 50)]

def kmeans_clustering(points, n_clusters):
    centers = [random.choice(points) for p in range(0, n_clusters)]
    count = 0
    while True:
        final_labels = [0] * len(points)
        count += 1
        for pidx, point in enumerate(points):
            dist = np.linalg.norm(point - centers[0])
            label = 0
            for cidx, center in enumerate(centers[1:]):
                d = np.linalg.norm(point - center)
                if d < dist:
                    label = cidx + 1
                    dist = d
            if label != final_labels[pidx]:
                final_labels[pidx] = label
        converged = True
        for cidx in range(0, n_clusters):
            pts = [point for pidx, point in enumerate(points)
                   if final_labels[pidx] == cidx]
            C = np.mean(pts, axis=0)
            if np.linalg.norm(C - centers[cidx]) > 0.01:
                converged = False
            centers[cidx] = C
        if converged:
            break
    return final_labels, centers

X = X0 + X1 + X2
Y = Y0 + Y1 + Y2
points = [np.array([x, y]) for x, y in zip(X, Y)]
labels, centers = kmeans_clustering(points, 3)


C0x = [point[0] for pidx, point in enumerate(points) if labels[pidx] == 0]
C0y = [point[1] for pidx, point in enumerate(points) if labels[pidx] == 0]
C1x = [point[0] for pidx, point in enumerate(points) if labels[pidx] == 1]
C1y = [point[1] for pidx, point in enumerate(points) if labels[pidx] == 1]
C2x = [point[0] for pidx, point in enumerate(points) if labels[pidx] == 2]
C2y = [point[1] for pidx, point in enumerate(points) if labels[pidx] == 2]

plt.scatter(C0x, C0y)
plt.scatter(C1x, C1y)
plt.scatter(C2x, C2y)
plt.scatter(centers[0][0], centers[0][1]) ; plt.annotate('C0', (centers[0][0], centers[0][1]))
plt.scatter(centers[1][0], centers[1][1]) ; plt.annotate('C1', (centers[1][0], centers[1][1]))
plt.scatter(centers[2][0], centers[2][1]) ; plt.annotate('C2', (centers[2][0], centers[2][1]))
plt.show()
