import numpy as np
from jax import jacfwd, jacrev

from lagrangian_polynomial import LagrangianPolynome


def candidate_trajectory(Ts, Xs, t):
    poly = LagrangianPolynome(Ts, Xs)
    return poly.eval(t)


def local_state(f, t):
    traj_pos = f(t)
    traj_speed_f = jacrev(f)
    traj_speed = traj_speed_f(t)
    traj_acc = jacfwd(traj_speed_f)(t)
    return t, traj_pos, traj_speed, traj_acc


Ts = [0.0, 1.0, 2.0, 3.0]
Xs = [0.0, 1.0, 1.0, 0.0]

print(np.array(local_state(lambda t: candidate_trajectory(Ts, Xs, t), 1.5)))
# [ 1.5    1.125  0.    -1.   ]
