import matplotlib.pyplot as plt
plt.style.use('grayscale')
import numpy as np

# Fonction de simulation
# utilisant la méthode d'Euler.
def simulate(nsteps, delta, L, C,
             Q_0, i_0):
    Qs = []
    Is = []
    us = []
    for step in range(0, nsteps):
        i_0 = i_0 + Q_0 / (L * C) * delta
        Q_0 = Q_0 - i_0 * delta
        u_0 = Q_0 / C
        Is.append(i_0)
        Qs.append(Q_0)
        us.append(u_0)
    return Is, us, Qs


# Conditions initiales
# choisies de manière arbitraire.
L = 0.3
C = 3e-4
Vc_0 = 3.3
Q_0 = C * Vc_0
current, tension, load = simulate(
    5000, 1e-3,
    L, L,
    Q_0, 0)

# Tracé de le courbe obtenue
# par simulation.
plt.plot(tension)
plt.xlabel('temps')
plt.ylabel('tension')
plt.legend()
plt.show()
