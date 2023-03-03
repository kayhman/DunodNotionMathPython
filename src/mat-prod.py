import numpy as np

# Cette fonction calcule
# le produit de B par A.
def mult(A, B):
  nligsA, ncolsA = len(A), len(A[0])
  nligsB, ncolsB = len(B), len(B[0]);
  res = [[0] * ncolsB for i in range(nligsA)];
  for i in range(0, nligsA):
    for j in range(0, ncolsB):
      res[i][j] = 0
      for k in range(0, ncolsA):
          res[i][j] += A[i][k] * B[k][j]
  return res

# Chaque ligne de la matrice A
# contient le trajet à vélo,
# le nombre de longueurs,
# et celui de levées.
A = [[15.2, 41, 51],
     [7.2,  0,  43],
     [10.2, 44, 63],
     [8.2,  0,  35],
     [5.2,  54, 43]]

# Chaque colonne contient le coût énergétique.
B = [[480.0], [100.0], [30.0]];

# le coût énergétique de chaque journée
# se calcule en multipliant A par B.
print(mult(A, B));
# > [[12926.0], [4746.0], [11186.0], [4986.0], [9186.0]]

# Le produit de matrices
# est défini par défaut dans numpy par {\em dot}.
print(np.array(A).dot(np.array([row[0] for row in B])))
# [12926.  4746. 11186.  4986.  9186.]
