# Cette fonction retourne true si a est un multiple de b.
# C'est-à-dire si a est différent de b,
# et si le reste de la division de a par b est 0.
def is_multiple(a, b):
  return a != b and a % b == 0


is_multiple(12, 3)
# -> true

is_multiple(13, 3)

# -> false


# Cette fonction passe au crible d'\'Eratosthène les n premiers entiers.
# Elle ne conserve que ceux qui ne sont pas des multiples des entiers les précédant.
def sieves(n):
  # Construisons un tableau des entiers de 2 à n.
  primes = list(range(2, n + 1))
  idx = 0
  while idx < len(primes):
    p = primes[idx]
    primes = list(filter(lambda x: not is_multiple(x, p), primes))
    idx = idx + 1
  return primes


print(sieves(19))
# -> 2  3  5  7  11  13  17  19
