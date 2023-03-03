import ctypes
import numpy as np

# Affichons le code de 42 sur 32 bits.
print("{0:32b}".format(42))
# > 00000000000000000000000000101010

# Sur 16 bits,
# l'entier naturel le plus grand
# vaut $2^{16}-1 = 65535$.
print("{0:14b}".format(65535))
# > 1111 1111 1111 1111
# Il n'y a pas assez de bits
# pour stocker un entier plus grand.
print(np.uint16(65536))
# > 0


reel = 0.3
# Affichons les 17 premières décimales.
print("{0:.17f}".format(reel))
# > 0.29999999999999999

# Les réels sont encodés sous la forme $s \times m \times 2^{e-127}$
# $s$ indique le signe et est codé sur le $1^{er}$ bit
# $e$ est l'exposant, et est codé sur 8 bits
# $m$ est la mantisse, et est codée sur les 23 octets suivants.
print(bin(ctypes.c_uint.from_buffer(ctypes.c_float(reel)).value))
# > '0b1111101 00110011001100110011010'

# Ré exprimons notre réel en base 10
# depuis son encodage selon la norme IEEE 754.
print((1.0 + 2.0**-3 +  2.0**-4 + 2.0**-7 + 2.0**-8 + 2.0**-11 + 2.0**-12 + 2.0**-15 + 2.0**-16 + 2.0**-19 + 2.0**-20 + 2.0**-22) * 2.0**-2)
# > 0.30000001192092896

# Idem, mais à l'aide des fonctions
# prédéfinies dans Python.
significand, exp = np.frexp(reel)
print(significand * 2.0**exp)
# > 0.3
