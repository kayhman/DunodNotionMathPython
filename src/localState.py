from jax import jacfwd

def local_state(f, t):
    traj_pos = f(t)
    traj_speed_f = jacrev(f)
    traj_speed = traj_speed_f(t)
    traj_acc = jacfwd(traj_speed_f)(t)
    return t, traj_pos, traj_speed, traj_acc
