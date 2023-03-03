import numpy as np
import matplotlib.pyplot as plt

# Cette fonction se charge de créer une
# fonction qui va linéariser f au voisinage
# de $x_0$.
def linearise(f, f_p, x_0):
    f_lin = lambda x: f(x_0) + f_p(x_0) * (x - x_0)
    return f_lin


f = lambda x: x**2 # x² est la fonction à linéariser
f_p = lambda x: 2*x # 2x est la dérivée de f(x)
x_0 = 1.0 # $x_0$ est le point de linéarisation
f_lin = lambda x: linearise(f, f_p, x_0)(x) # $f_{lin}(x)$ est la linéarisation de f(x) au voisinage de $x_O$

xs = np.linspace(-3, 3, 100)
ys = [f(x) for x in xs]
xs2 = np.linspace(0, 3, 100)
f_lin_x_1 = [f_lin(x) for x in xs2]
plt.plot(xs, ys, xs2, f_lin_x_1, '-.',
         [x_0], f(x_0), 'o')
plt.show()
