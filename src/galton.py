import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('grayscale')

# Cette fonction suit la chute d'une bille
# et compte le nombre de fois où elle choisit le chemin de gauche.
def galton_drop(depth):
    nb_left = 0
    for i in range(0, depth):
        direction = np.random.choice(['L', 'R'])
        if direction == 'L':
            nb_left += 1
    return nb_left

# Cette fonction simule le lancer
# de $nb_{balls}$ sur une planche de Galton
# à $depth$ niveau.
def galton_board(nb_balls, depth):
    counter = {idx: 0 for idx in range(0, depth+1)}
    for ball in range(nb_balls):
        nb_left = galton_drop(depth)
        counter[nb_left] += 1
    # Normalisation
    keys = list(counter.keys())
    for key in keys:
        counter[(key - depth/2) / depth] = counter.pop(key) / nb_balls

    return counter

# Cette fonction dessine une planche de Galton.
def draw_galton_board(depth):
    X = []
    Y = []
    for step in range(0, depth):
        X += [-step / 2.0 + point for point in range(0,step+1)]
        Y += [-step for _ in range(0,step+1)]

    plt.scatter(X, Y)
    plt.xlabel('Planche de Galton')
    plt.show()

depth = 30
counter = galton_board(20000, depth)
X = np.linspace(-0.6, 0.6, 100)
plt.bar(counter.keys(), counter.values(), label='nombre de billes par cellule', width=1.0 / (3*depth))
plt.plot(X, [1/math.sqrt(2 * math.pi) * math.exp(-1/2.0 * x**2) for x in X])
plt.xlabel('cellules')
plt.legend()
plt.show()
print(max(counter.keys()))

draw_galton_board(10)
