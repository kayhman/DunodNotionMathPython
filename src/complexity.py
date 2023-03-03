import matplotlib.pyplot as plt
from functools import reduce
import random
import math
# Classe permettant de compter
# le nombre d'appels à un opérateur.
class MyFloat:
    nb_cmp = 0
    def __init__(self, val):
        self.value = val
    def __gt__(self, b):
        MyFloat.nb_cmp += 1
        return self.value > b.value
    def __ge__(self, b):
        MyFloat.nb_cmp += 1
        return self.value >= b.value
    def __lt__(self, b):
        MyFloat.nb_cmp += 1
        return self.value < b.value
    def __le__(self, b):
        MyFloat.nb_cmp += 1
        return self.value <= b.value
    def __str__(self):
        return str(self.value)
# Implémentation du tri par
# fusion.
def sort(vals):
    nb_vals = len(vals)
    if nb_vals == 1:
        return vals
    if nb_vals == 2:
        if vals[0] < vals[1]:
            return vals
        return [vals[1], vals[0]]
    head = sort(vals[:nb_vals//2])
    tail = sort(vals[nb_vals//2:])
    return merge(head, tail)
# Le code de fusion
# entre les deux sous-tableaux.
def merge(la, lb):
    aidx = 0
    bidx = 0
    while bidx < len(lb) and aidx < len(la):
        if lb[bidx] < la[aidx]:
            la.insert(aidx, lb[bidx])
            bidx += 1
        elif lb[bidx] >= la[aidx]:
            if aidx == len(la) - 1:
                la.insert(aidx+1, lb[bidx])
                bidx += 1
            else:
                aidx += 1
        elif lb[bidx] > la[aidx] and lb[bidx] <= la[aidx+1]:
            la.insert(aidx+1, lb[bidx])
            bidx += 1
    return la

complexity = []
Xs = []
for n in range(10, 5000):
    MyFloat.nb_cmp = 0
    vals = [MyFloat(random.randint(0, 100)) for i in range(0, n)]
    sorted = sort(vals)
    nb_ops = MyFloat.nb_cmp
    complexity.append(nb_ops)
    Xs.append(n)

plt.plot(Xs, Xs, label='lineaire')
plt.plot(Xs, [n * math.log(n) for n in Xs], label='nlog(n)')
plt.plot(Xs, complexity, label='nombre de comparaisons')
plt.legend()
plt.show()
