import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

# Calcul des paramètres par la méthode des moindres carrés.
def fit(X, Y):
    return inv(X.T.dot(X)).dot(X.T).dot(Y)

# Le rayon des pales de l'éolienne est de 50\:m.
R = 50
# La surface qui en découle est $S = S \pi r^2$.
S = 2 * 3.1415 * R**2

# La vitesse du vent est prise entre 0 et 30 $\frac{m}{s}$.
V = np.linspace(0, 30, 50)
V_3 = 8.0 / 27.0 * S * np.array([[v**3] for v in V])
# Masse volumique de l'air
rho = 1.292
# Calcul de la puissance selon la loi de Betz, en ajoutant du bruit gaussien.
P = np.array([ rho * (V_3+np.random.normal())])

# Pour l'exercice, la méthode des moindres carrés
# est utilisée pour déterminer $\rho$.
rho = fit(V_3, P)
print(rho)
# [[[1.29200001]]]

plt.plot(V,
         [p[0] for p in P[0]],
         label='Loi de Betz')
plt.legend()
plt.show()
