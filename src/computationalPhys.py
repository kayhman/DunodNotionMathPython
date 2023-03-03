import scipy.integrate as integrate
import numpy as np
import jax.numpy as jnp
from jax import jacfwd, jacrev, jit

from lagrangian_polynomial import LagrangianPolynome


def local_state(f, t):
    traj_pos = f(t)
    traj_speed_f = jacrev(f)
    traj_speed = traj_speed_f(t)
    traj_acc = jacfwd(traj_speed_f)(t)
    return t, traj_pos, traj_speed, traj_acc

def lagrangian(local_state):
    t, x, v, a = local_state
    return abs(0.5 * jnp.dot(v, v) - A * x)

def action(lagrangian, trajectory, t0, t1):
    return integrate.quad(lambda t: lagrangian(local_state(trajectory, t)), t0, t1)

A = -9.81
x_0 = 0.0

@jit
def candidate_trajectory(Ts, Xs, t):
    poly_Xs = LagrangianPolynome(Ts, np.append(np.array([x_0]), Xs))
    return poly_Xs.eval(t)

def real_trajectory(Ts, Xs, t):
    return 1/2.0 * A * t * t


t0 = 0.0
t1 = 4.0

Ts = [t0, 1.0, 4.0]
Xs = [real_trajectory(None, None, 1.0),
      real_trajectory(None, None, 5.0)]

act = action(lagrangian, lambda t: candidate_trajectory(Ts, Xs, t), t0, t1)
print(act)
# (1157.8405356289313, 1.4060696690905207e-05)


# we introduce error in the trajectory
Xs = [real_trajectory(None, None, 1.0) - 30.0,
      real_trajectory(None, None, 5.0) + 25]

act = action(lagrangian, lambda t: candidate_trajectory(Ts, Xs, t), t0, t1)
# action value is increased
print(act)
# (1872.2112206943714, 7.245376117678251e-05)
