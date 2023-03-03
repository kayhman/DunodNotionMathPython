# L'installation se fait avec pip : pip install matplotlib
# L'import de la librairie se fait avec
import matplotlib.pyplot as plt
import random

# Le tracé d'un nuage de points se fait comme suit
X = [random.random() - 0.5 for i in range(0, 100)]
Y = [random.random() - 0.5 for i in range(0, 100)]
plt.scatter(X, Y)
plt.show()

# Le tracé d'une courbe se fait comme suit
X = [i for i in range(-50, 50)]
Y = [x**2 for x in X]
plt.plot(X, Y)
plt.show()
