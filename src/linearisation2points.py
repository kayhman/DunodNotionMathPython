import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**2 # x² est la fonction à linéariser.
x_1 = -1.0
x_2 = 1.0

x_3 = 1.0
x_4 = 2.0

xs = np.linspace(-3, 3, 100)
ys = [f(x) for x in xs]
plt.plot(xs, ys,
         [x_1], f(x_1), 'o',
         [x_2], f(x_2), 'o',
         [x_1, x_2], [f(x_1), f(x_2)], '-',
         [x_3], f(x_3), 'o',
         [x_4], f(x_4), 'o',
         [x_3, x_4], [f(x_3), f(x_4)], '-',
)
plt.show()
