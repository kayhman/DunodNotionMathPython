import matplotlib.pyplot as plt
import jax.numpy as jnp
import numpy as np
import jax
from jax import grad, jacfwd, jacrev, jit

from scipy.optimize import minimize, root

from lagrangian_polynomial import LagrangianPolynome
from integration import integrate, integrate_num


A = -9.81
x_0 = 0.0

def candidate_trajectory(Ts, Xs, t):
    poly_Xs = LagrangianPolynome(Ts, np.append(np.array([x_0]), Xs))
    return poly_Xs.eval(t)

def real_trajectory(Ts, Xs, t):
    return 1/2.0 * A * t * t


def local_state(f, t):
    traj_pos = f(t)
    traj_speed_f = jacrev(f)
    traj_speed = traj_speed_f(t)
    return t, traj_pos, traj_speed, None

def lagrangian(local_state):
    t, x, v, a = local_state
    return abs(0.5 * jnp.dot(v, v) - A * x)

t0 = 0.0
t1 = 4.0

Ts = [t0, 1.0, 4.0]
Xs = [real_trajectory(None, None, 1.0) - 30.0,
      real_trajectory(None, None, 5.0) + 25]



# plot initial candidate trajectory
times = np.linspace(t0, t1, 40)
traj = [candidate_trajectory(Ts, Xs, t) for t in times]
plt.plot(times, [x for x in traj], 'b', label='initial candidate trajectory')
plt.plot(times,
         np.vectorize(lambda t: real_trajectory(Ts, Xs, t))(times), 'o', label='check point')

action_integrande = lambda t, Xp : lagrangian(local_state(lambda lt : candidate_trajectory(Ts, Xp, lt), t))

action = lambda Xp, t0, t1: integrate(lambda t: action_integrande(t, Xp), t0, t1, 100)

best = minimize(lambda Xc : action(Xc, t0, t1),
                Xs,
                method='Nelder-Mead',
                )

traj = [candidate_trajectory(Ts, best.x, t) for t in times]
plt.plot(times, [x for x in traj], label='final trajectory')
plt.legend()
plt.show()
