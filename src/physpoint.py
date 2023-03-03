import matplotlib.pyplot as plt
plt.style.use('grayscale')
import numpy as np

x0 = 4.0
y0 = 4.0
v0x = 1.0
v0y = 0.0

# Valeur de la gravité sur Terre.
a = -9.81

# \'Equation du mouvement
# obtenue en intégrant les équations
# différentielles.
x = lambda t: x0 + v0x * t
y = lambda t: y0 + v0y * t + 1/2 * a * t * t

ts = np.linspace(0, 0.1, 100)
xs = [x(t) for t in ts]
ys = [y(t) for t in ts]

plt.plot(xs, ys)
plt.show()

# Fonction de simulation
# utilisant la méthode d'Euler.
def simulate(nsteps, delta, masse, forces,
             x_0, v_0):
    x_t = x_0
    v_t = v_0
    xs = []
    vs = []
    for step in range(0, nsteps):
       acc = forces(x_t, v_t, masse) / masse
       v_t = v_t + acc * delta
       x_t = x_t + v_t * delta
       xs.append(x_t)
       vs.append(v_t)
    return xs, vs

# Définition d'une force simulant
# la gravité $f = m \cot g$.
def gravity(x_t, v_t, m):
    return np.array([0, a * m])

x_0 = np.array([0, 0])
v_0 = np.array([1, 0])
traj, vel = simulate(100, 1e-3, 1, gravity, x_0, v_0)

# Tracé de le courbe obtenue
# par simulation.
plt.plot([x[0] for x in traj], [x[1] for x in traj])
plt.show()
