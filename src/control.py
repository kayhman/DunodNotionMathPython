import matplotlib.pyplot as plt
import numpy as np

def simulate(nsteps, delta, masse, forces,
             x_0, v_0):
    x_t = x_0
    v_t = v_0
    xs = []
    vs = []
    for step in range(0, nsteps):
        acc = np.array([0, 0])
        for force in forces:
            acc = acc + force(x_t, v_t, masse) / masse
        v_t = v_t + acc * delta
        x_t = x_t + v_t * delta
        xs.append(x_t)
        vs.append(v_t)
    return xs, vs

def control(x_t, v_t, m):
    target_y = 4.0
    coeff = 100.0
    delta_y = target_y - x_t[1]
    ctrl_y = coeff * delta_y
    return np.array([0, ctrl_y])

# Simulation d'une chute libre
# avec contrôle de l'altitude
# par asservissement proportionnel.
x_0 = np.array([0, 4])
v_0 = np.array([1, 0])
traj, vel = simulate(1000, 1e-3, 1, [gravity, control], x_0, v_0)

plt.plot([x[0] for x in traj], [x[1] for x in traj])
plt.xlabel('Abscisse x')
plt.xlabel('Ordonnee y')
plt.legend()
plt.show()

def control(x_t, v_t, m):
    target_y = 4.0
    coeff_p = 100.0
    coeff_d = -5.0
    delta_y = target_y - x_t[1]
    ctrl_y = coeff_p * delta_y + coeff_d * v_t[1]
    return np.array([0, ctrl_y])

# Simulation d'une chute libre
# avec contrôle de l'altitude
# par asservissement proportionnel dérivé.
x_0 = np.array([0, 4])
v_0 = np.array([1, 0])
traj, vel = simulate(1000, 3e-3, 1, [gravity, control], x_0, v_0)

plt.plot([x[0] for x in traj], [x[1] for x in traj])
plt.xlabel('Abscisse x')
plt.xlabel('Ordonnee y')
plt.legend()
plt.show()
