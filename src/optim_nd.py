from math import copysign
import math
from collections import namedtuple
import numpy as np

Constraint = namedtuple('Constraint', ['ori', 'dir', 'gap', 'name'])

def normalize_constraint(const: Constraint):
    norm = np.linalg.norm(const.dir)
    return Constraint(const.ori,
                      const.dir / norm,
                      const.gap / norm,
                      const.name)

def constraint_distance(x, cst: Constraint):
    dist = (x - cst.ori).dot(cst.dir)
    return dist - cst.gap


def project(x, cst: Constraint):
    x = x - ((x - cst.ori).dot(cst.dir) + cst.gap) * cst.dir
    return x


def constrained(x, constraints):
    for constraint in constraints:
        dist = constraint_distance(x, constraint)
        # project onto constraint space if constraint is not respected
        if dist > 0: # constraint.gap
            x = project(x, constraint)
    return x, dist


def maximize(weights, constraints, x_0, delta):
    nb_iter = 0
    obj = weights.dot(x_0)
    while True:
        prev_x = x_0.copy()
        for dim in range(0, len(weights)):
            x_0[dim] += delta * weights[dim]
            x_0 , dist = constrained(x_0, constraints)
        nb_iter += 1
        if np.linalg.norm(prev_x - x_0) <  1e-7:
            break
    return x_0, nb_iter


p1 = np.array([3, 0, 0, 0])
n1 = np.array([1, 0, 0, 0])

p2 = np.array([0, 4, 0, 0])
n2 = np.array([0, 1, 0, 0])

p3 = np.array([0, 4, 4, 0])
n3 = np.array([0, 1, 1, 0])

p4 = np.array([0, 0, 0, 5])
n4 = np.array([0, 0, 0, 1])

c1 = Constraint(p1, n1, 0.0, 'max_W')
c2 = Constraint(p2, n2, 0.0, 'max_L')
c3 = Constraint(p3, n3, 0.0, 'max_sum_L_H')
c4 = Constraint(p4, n4, 0.0, 'max_Z')


c3 = normalize_constraint(c3)

x = np.array([1, 1, 0.8, 6.0])
delta = 1e-2

weights = np.array([1., 1., 1., 1.])

x_opt, nb_iter = maximize(weights,
                          [c1, c2, c3, c4],
                          x, delta)

print('max obj', x_opt.dot(weights), 'in', nb_iter)
# -> max obj 11.0 in 338
print('point', x_opt)
# -> point  [3.         3.99000004 4.00999996]
