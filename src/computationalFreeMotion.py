import matplotlib.pyplot as plt
import jax.numpy as jnp
import numpy as np
from jax import grad, jacfwd, jacrev, jit

from lagrangian_polynomial import LagrangianPolynome
from integration import integrate
from scipy.optimize import minimize, root

A = -9.81

@jit
def candidate_trajectory(Ts, Xs, Ys, t):
    poly_Xs = LagrangianPolynome(Ts, jnp.append(np.array([0.0]), jnp.append(Xs, np.array([4.0]))))
    poly_Ys = LagrangianPolynome(Ts, jnp.append(np.array([0.0]), jnp.append(Ys, np.array([0.0]))))
    return jnp.array([poly_Xs.eval(t), poly_Ys.eval(t)])

def real_trajectory(Ts, Xs, Ys, t):
    return [t, A/2.0 * t*t - 2.0 * A * t]

def local_state(f, t):
    traj_pos = f(t)
    traj_speed_f = jacfwd(f)
    traj_speed = traj_speed_f(t)
    return t, traj_pos, traj_speed, None

def lagrangian(local_state):
    t, x, v, a = local_state
    return 0.5 * jnp.dot(v, v) + A * x[1]

t0 = 0.0
t1 = 4.0
n = 2

Ts = [t0] + [2.0, 3.0]  + [t1]
Xs = jnp.array([2.0, 3.0])
Ys = jnp.array([real_trajectory(None, None, None, 2.0)[0] * 0.3,
                real_trajectory(None, None, None, 3.0)[0] * 0.5])
times = np.linspace(0.0, 4.0, 40)
plt.plot(np.vectorize(lambda t: candidate_trajectory(Ts, Xs, Ys, t)[0])(times),
         np.vectorize(lambda t: candidate_trajectory(Ts, Xs, Ys, t)[1])(times), 'b')

plt.plot(np.vectorize(lambda t: real_trajectory(Ts, Xs, Ys, t)[0])(times),
         np.vectorize(lambda t: real_trajectory(Ts, Xs, Ys, t)[1])(times), 'o')

action_integrande = lambda t, Xs, Ys : lagrangian(local_state(lambda lt : candidate_trajectory(Ts, Xs, Ys, lt), t))

action = lambda Xs, Ys, t0, t1: integrate(lambda t: action_integrande(t, Xs, Ys), t0, t1, 100)

best = minimize(lambda Ys : action(Xs, Ys, t0, t1),
                Ys,
                method='Nelder-Mead',
                )

Ys = jnp.array(best.x)
plt.plot(np.vectorize(lambda t: candidate_trajectory(Ts, Xs, Ys, t)[0])(times),
         np.vectorize(lambda t: candidate_trajectory(Ts, Xs, Ys, t)[1])(times))
plt.show()
