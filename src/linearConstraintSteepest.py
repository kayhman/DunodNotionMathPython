def maximize(weights, x_0, delta):
    nb_iter = 0
    while True:
        prev_x = x_0.copy()
        for dim in range(0, len(weights)):
            x_0[dim] += delta * weights[dim]
        nb_iter += 1
        if np.linalg.norm(prev_x - x_0) <  1e-7:
            break
    return x_0, nb_iter
