from skimage import data, io
import numpy as np

# Récupération d'une image depuis la librairie Skimage.
image = data.brick()
# Les images sont chargées sous la forme de tableau Numpy.
# Ce qui est pratique pour les manipuler.
print(type(image))
#> <class 'numpy.ndarray'>
# Sauvegarde de l'image.
io.imsave('test.png', image)
