import numpy as np
import matplotlib.pyplot as plt
plt.style.use('grayscale')

n = 1.0 # quantité de matière en mole.
R = 8.314 # constante en J K\textsuperscript{-1} mol\textsuperscript{-1}

# Calcul de la pression selon la
# température et le volume.
def pression(T, V):
    return n * R * T / V

# Calcul du volume selon la
# température et le volume.
def volume(T, P):
    return n * R * T / P

# Calcul de la température selon la
# pression et le volume.
def temperature(P, V):
    return P * V / (n * R)

# Conditions normales de température et
# de pression.
T0 = 273.15 # en Kelvin, soit 0° Celsius
P0 = 101325 # en Pascal, soit 1 atmosphère

# \`A l'aide de ces quelques fonctions
# il est facile de mener des expériences virtuelles.

# Par exemple, on obtient simplement le volume
# occupé par une mole de gaz dans les conditions
# normales :
print(volume(T0, P0))
#> 0.022412722427831235 (en litre)

# On peut vérifier que la température est
# la bonne pour la pression normale
# et le volume normal :
print(temperature(P0,volume(T0, P0)))
#> 273.15

# En doublant la pression
# la température devient :
print(temperature(2 * P0,
                  volume(T0, P0)))
#> 546.3


vs = np.linspace(0.01, 1, 100)
plt.plot(vs,
         [pression(T0, v) for v in vs],
         label='')
plt.xlabel('Volume')
plt.ylabel('Pression')
plt.legend()
plt.show()
