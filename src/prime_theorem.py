from math import log
from sieves import sieves
import matplotlib.pyplot as plt

# Nous créons ici un tableau des entiers de 10 à 1 000 000, de 10 en 10.
max = 10000
ns = [n for n in range(10, max, 10)]
# -> 500-element Vector{Int64}:10 20 30 40 50 ... 5000.

# Nous calculons pour ces derniers le ratio $\frac{\pi(n)}{n}$.
primes = sieves(max)
pi = [len([x for x in primes if x <= n]) for n in ns]
freq = [pi[i] / n for (i, n) in enumerate(ns)]
chck = [freq[i] * log(i+1)  for (i, n) in enumerate(ns)]

# Et nous traçons la courbe de ce ratio en fonction de n.
plt.plot(ns, chck)
plt.show()
