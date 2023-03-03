from functools import reduce
import numpy as np
import jax.numpy as jnp


class LagrangianPolynome:
    def __init__(self, Ts, Xs):
        self.Ts = Ts
        self.Xs = Xs

    def numerator(self, idx, t):
        coef = reduce(lambda a, b: a * b,
                      [(t - t_i) for t_idx, t_i in enumerate(self.Ts) if t_idx != idx], 1.0)
        return coef * self.Xs[idx]

    def denominator(self, idx):
        return np.multiply.reduce([(self.Ts[idx] - t_i)
                                   for t_idx, t_i
                                   in enumerate(self.Ts) if t_idx != idx])

    def eval(self, t):
        val = 0.0
        for idx in range(len(self.Ts)):
            val += self.numerator(idx, t) / self.denominator(idx)
        return val
