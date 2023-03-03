import matplotlib.pyplot as plt
plt.style.use('grayscale')
from math import pi, e

# Vérification de la formule d'Euler.
print(e**(1j * pi).real)
#> 1.0


# Intuition sur le sens de la formule
# et l'esthétique sous-jacente.
def plot_exponential_approximation(n):
    p_0 = 1 + 0j
    r = 1 + pi/n * 1j
    p_im1 = p_0
    p_i = p_0
    for i in range(0, n):
        print(p_i)
        plt.plot([0, p_i.real], [0, p_i.imag])
        p_i = p_i * r
        plt.plot([p_im1.real, p_i.real], [p_im1.imag, p_i.imag])
        p_im1 = p_i
    plt.plot([0, p_i.real], [0, p_i.imag])
    plt.axis('equal')
    plt.show()

plot_exponential_approximation(8)
