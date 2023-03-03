from numpy.random import multivariate_normal
import matplotlib.pyplot as plt
plt.style.use('grayscale')
plt.gca().set_aspect('equal', adjustable='box')
import numpy as np

# Décomposition en composantes
# principales
def PCA(X):
    # Calcul de la moyenne
    # pour chaque dimension
    means = np.matrix([np.mean(X[:, col])
                       for col in range(0, X.shape[1])])
    # Recentrage sur la
    # moyenne
    X = X - np.ones((X.shape[0], 1)) * means
    # Calcul de la covariance
    C = 1/(X.shape[0] - 1) * X.T * X
    # Extraction des composantes
    # principales par le calcul
    # des vecteurs propres
    ew, ev = np.linalg.eig(C)
    return X, ew, ev


data = np.matrix(multivariate_normal([7, 8],
                                     [[5, 1],
                                      [1, 1]],
                                     500))
centered, ew, ev = PCA(data)

print(ew)


plt.scatter(list(data[:, 0]),
            list(data[:, 1]), label='Nuage de point initial')
plt.scatter(list(centered[:, 0]),
            list(centered[:, 1]), label='Nuage de point recentre')
plt.quiver(0, 0, ev[0, 0], ev[1, 0], scale=1/ew[0], scale_units='x')
plt.quiver(0, 0, ev[0, 1], ev[1, 1], scale=1/ew[1], scale_units='x')

plt.legend()
plt.show()
