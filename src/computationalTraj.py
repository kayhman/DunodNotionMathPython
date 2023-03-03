import numpy as np
import matplotlib.pyplot as plt

from lagrangian_polynomial import LagrangianPolynome

Ts = [0.0, 1.0, 2.0, 3.0]
Xs = [0.0, 1.0, 1.0, 0.0]

poly = LagrangianPolynome(Ts, Xs)

# Check key values
print(poly.eval(0.0))
print(poly.eval(1.0))
print(poly.eval(2.0))
print(poly.eval(3.0))

times = np.linspace(0.0, 3.0, 40)
traj = [poly.eval(t) for t in times]
plt.plot(Ts, Xs, 'o')
plt.plot(times, traj)
plt.show()
