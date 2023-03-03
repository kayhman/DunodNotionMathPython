from math import floor


# Construction de la table de logarithmes
# pour les nombres de 1.0 à 1e-7.
# La position dans le tableau correspond alors à l'exposant.
def log_table(min):
  # r est ici une approximation de e, la constante d'Euler.
  # C'est la base des logarithmes de nos ordinateurs.
  r = (1 - 1 / 10**7)
  table = []
  i = 1
  s = 1
  while True:
    table.append(s)
    s = s * r
    i = i + 1
    if s < min:
      break
  return table


# Recherche dans la table du logarithme le plus proche de v.
# L'indice de cette valeur dans la table donne l'exposant.
# La méthode employée pour la recherche est la dichotomie.
def lookup(table, v):
  up = len(table) - 1
  low = 0
  middle = round((up + low) / 2)
  idx = 1
  while True:
    if v <= table[low] and v > table[middle]:
      # La valeur se trouve entre le début et le milieu du tableau.
      # Nous restreignons la recherche à cette zone.
      up = middle
    else:
      # Sinon la valeur se trouve entre le milieu et la fin du tableau.
      # Nous restreignons la recherche à cette zone.
      low = middle

    # Nous mettons à jour la position du milieu.
    middle = round((up + low) / 2)
    if up - low == 1:
      # Il n'y a plus qu'une valeur dans la zone de recherche.
      # Nous avons trouvé notre exposant.
      return middle
  # Si nous en arrivons là, nous n'avons rien trouvé.
  return -1


ln = log_table(1e-7)
v1 = 0.0004560
v2 = 0.0076890
l1 = lookup(ln, v1)
l2 = lookup(ln, v2)
print(l1, l2, len(ln))
print(ln[l1], ln[l2], ln[0], ln[-1], len(ln))
prod = ln[l1 + l2]
check = v1 * v2

print("log: ", int(floor(prod * 1e14)), ", reelle : ",
      int(floor(check * 1e14)))
print("erreur: ", abs(int(floor(prod * 1e14)) - int(floor(check * 1e14))))
# nous obtenons une valeur approchée très proche.
# > log: 350618389, réelle : 350618400
