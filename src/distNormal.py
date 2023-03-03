import numpy as np
from math import pi, sqrt, exp
import matplotlib.pyplot as plt

# Définition de la fonction
# de distribution normale
f = lambda sigma, mu, x: 1.0 / (sigma * sqrt(2*pi)) * exp(-0.5 * ((x - mu)/sigma)**2)

# Tracé de la distribution
# normale standard avec $\mu = 0$ et $\sigma = 1$
sigma = 1.0
mu = 0

X = np.linspace(-5, 5, 100)
Y = [f(sigma, mu, x) for x in X]

plt.plot(X, Y)
plt.show()

# Définition de la version multi valuée
# de la gaussienne, utilisée pour calculer $\mathbb{P}(A \cap B)$
mnv = lambda Sigma, Mu, x: 1.0/np.linalg.det(2*pi*Sigma)**2 * exp(-0.5 * ((x - Mu).T * np.linalg.inv(Sigma) * (x - Mu)))

sigma_A = 1.0
mu_A = 0
sigma_B = 1.0
mu_B = 0

Sigma = np.matrix([[sigma_A, 0], [0, sigma_B]])
Mu = np.matrix([[mu_A], [mu_B]])


x_b = 0
X = np.linspace(-7, 7, 100)
Y_AnB = [mnv(Sigma, Mu, np.array([[x], [x_b]])) for x in X]
Y_B = [f(sigma_B, mu_B, x_b) for x in X]


# La distribution pour la
# probabilité conditionnelle est calculée ici
Y_cond = [(yanb) / yb for yanb, yb in zip(Y_AnB, Y_B)]


# Et affichée là.
plt.plot(X, Y_cond)
plt.show()
