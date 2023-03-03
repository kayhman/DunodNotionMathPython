from functools import reduce
from math import exp

class Neuron:
    def __init__(self, name, weights, activation):
        self.name = name
        self.weights = weights
        self.activation = activation
        self.sum = None
        self.entry = None

    def output(self, entry):
        self.entry = entry
        sum = reduce(lambda a, b : a + b,
                     [self.weights[i] * entry[i] for i in range(0, len(entry))])
        self.sum =  sum
        return self.activation(sum)

    def __str__(self):
        return self.name + ": " + str(self.weights)

class Network:
    def __init__(self, layers):
        self.layers = layers

    def output(self, entry):
        for layer in self.layers:
            new_entry = [1.] # biais
            for neuron in layer:
                out = neuron.output(entry)
                new_entry.append(out)
            entry = new_entry
        return out

def sigmoid(x):
    return 1 / (1 + exp(-x))

n1_l1 = Neuron("n1_l1", [-4, 10, 10], sigmoid) # or
n2_l1 = Neuron("n2_l1", [9, -6, -6], sigmoid) # nand
n1_l2 = Neuron("n1_l2", [-16, 10, 10], sigmoid) # and

layer1 = [n1_l1, n2_l1]
layer2 = [n1_l2]

network = Network([layer1, layer2])


print(network.output([1, 0, 1]))
# > 0.9707166363167491
print(network.output([1, 1, 0]))
# > 0.9707166363167491
print(network.output([1, 0, 0]))
# > 0.002954780238219401
print(network.output([1, 1, 1]))
# > 0.002954780238219401
