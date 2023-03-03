import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

# Calcul des paramètres par la méthode des moindres carrés.
def fit(X, Y):
    return inv(X.T.dot(X)).dot(X.T).dot(Y)

# La relation recherchée ici est du type $ y = a * x $, avec $a \approx 1.0$.
X = np.array([[3.1], [1.01], [1.98], [2.02], [2.93], [3.07]])
Y = np.array([2.9, 0.9, 2.3, 2.05, 2.8, 3.12])

linear_params = fit(X, Y)
print(linear_params)
# > [0.99278671]

# La relation recherchée ici est du type $ y = a * x + b $, avec $a \approx 1.0$ et $b \approx 0.0$.
X = np.array([[1, 3.1], [1, 1.01], [1, 1.98], [1, 2.02], [1, 2.93], [1, 3.07]])
affine_params = fit(X, Y)
print(affine_params)
# > [0.10908029
#    0.95078088]

# Tracé de la courbe.
plt.scatter([x[1] for x in X], Y)
plt.plot(np.linspace(1, 3, 10),
         np.linspace(1, 3, 10) * linear_params[0],
         ':', label='lineaire')
plt.plot(np.linspace(1, 3, 10),
         np.linspace(1, 3, 10) * affine_params[1] + affine_params[0],
         '-.', label='affine')
plt.legend()
plt.show()
