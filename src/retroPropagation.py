from functools import reduce
from math import exp
import random

class Neuron:
    def __init__(self, name, weights, activation, activation_derivative):
        self.name = name
        self.weights = weights
        self.activation = activation
        self.activation_derivative = activation_derivative
        self.sum = None
        self.entry = None

    def output(self, entry):
        # voir le code page \pageref{neural}

    def update_weights(self, error, alpha):
        lerr = self.activation_derivative(self.sum) * error
        for idx, _ in enumerate(self.weights):
            # La mise à jour des poids se fait en
            # multipliant l'erreur de la couche suivante
            # par l'entrée correspondante du neurone.
            delta =  lerr * self.entry[idx]
            self.weights[idx] += - delta * alpha
        # L'erreur du neurone courant est retournée
        # afin de servir comme erreur de sortie
        # du neurone précédent.
        return lerr

class Network:
    def __init__(self, layers):
        self.layers = layers

    def output(self, entry):
        # voir le code page \pageref{neural}

    def update_weights(self, error, alpha):
        for lidx, layer in enumerate(reversed(self.layers)):
            lerror = error[lidx]
            new_error = []
            for idx, neuron in enumerate(layer):
                err = neuron.update_weights(lerror[idx], alpha)
                # L'erreur du neurone courant
                # est multipliée par le poids le reliant
                # au neurone précédent.
                new_error.append([err * weight for weight in neuron.weights[1:]])
            error += new_error

def sigmoid(x):
    return 1 / (1 + exp(-x))
def sigmoid_derivative(x):
    return exp(-x) / (1 + exp(-x))**2

# Application de la rétropropagation
# à l'apprentissage de la fonction $xor$.
n1_l1 = Neuron('or', [-1, 10, 10], sigmoid, sigmoid_derivative) # or
n2_l1 = Neuron('nand', [1, -0.5, -0.5], sigmoid, sigmoid_derivative) # nand
n1_l2 = Neuron('and', [-1, 1, 1], sigmoid, sigmoid_derivative) # and

layer1, layer2 = [n1_l1, n2_l1], [n1_l2]

network = Network([layer1, layer2])

train_set = {"0x0": ([1, 0, 0], 0), "0x1": ([1, 0, 1], 1),
             "1x0": ([1, 1, 0], 1), "1x1": ([1, 1, 1], 0)}

for i in range(0, 100000):
    key = random.choice(list(train_set.keys()))
    inpt, real = train_set[key]
    pred = network.output(inpt)
    network.update_weights([[2 * (pred - real)]], 0.1)

for key, values in train_set.items():
    inpt, real = values
    pred = network.output(inpt)
    print(key, real, pred)
