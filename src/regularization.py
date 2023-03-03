import numpy as np
import matplotlib.pyplot as plt
plt.style.use('grayscale')

x = np.linspace(-20, 20, 200)
# La valeur absolue de x est calculée
y = np.abs(x)
# Ici une approximation de la valeur absolue de x est calculée
# avec le log(cosh)
y_logcosh = np.log(np.cosh(x))
plt.plot(x, y, label=f'Error absolue')
plt.plot(x, y_logcosh, label=f'log(cosh)')
plt.legend(loc='upper left')
plt.show()

# En zéro, les deux fonctions
# valent bien 0
print(np.abs(0.0))
#> 0.0
print(np.log(np.cosh(0)))
#> 0.0

# Pour une valeur suffisamment positive
# l'écart entre les deux est bien log(2)
print(np.log(np.cosh(10)) - 10 + np.log(2))
#> 2.0611529150116326e-09

# La même chose est valable
# pour une valeur suffisamment négative
print(np.log(np.cosh(-10)) - 10 + np.log(2))
#> 2.0611529150116326e-09
