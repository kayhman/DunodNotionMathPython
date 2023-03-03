class DecisionNode:
    # Classe de n\oe ud de decision.
    # Il s'agit d'un simple n\oe ud binaire, avec potentiellement deux enfants : gauche et droite.
    # Le n\oe ud gauche est renvoyé lorsque la condition est vraie.
    # Le n\oe ud False est renvoyé lorsque la condition est fausse.
    def __init__(self, name, condition, value=None):
        self.name = name
        self.condition = condition
        self.value = value
        self.left = None
        self.right = None

    def add_left_node(self, left):
        self.left = left

    def add_right_node(self, right):
        self.right = right

    def is_leaf(self):
        # Un n\oe ud sans enfant est une feuille
        return (not self.left) and (not self.right)

    def next(self, data):
        # Retourne le n\oe ud a parcourir en fonction du resultat du test
        cond = self.condition(data)
        if cond:
            return self.left
        else:
            return self.right


class DecisionTree:
    # Un DecisionTree est un modèle qui fournit des prédictions en fonction de l'entrée.
    # Une prediction est la somme des valeurs des feuilles, pour les feuilles qui ont été activées par l'entrée.
    def __init__(self, root):
        self.root = root

    def predict(self, data):
      child = root
      while child and not child.is_leaf():
        child = child.next(data)
      return child.value


root = DecisionNode('root', lambda d : d['A'] > 2.0)
root_left = DecisionNode('root_left', lambda d : d['B'] > 10.0, None)
root_right = DecisionNode('root_right', None, 1)
left_left = DecisionNode('left_left', None, 2)
left_right = DecisionNode('left_right', None, 3)

root.add_left_node(root_left)
root.add_right_node(root_right)

root_left.add_left_node(left_left)
root_left.add_right_node(left_right)

tree = DecisionTree(root)
print(tree.predict({'A' : 1, 'B' : 1})) # 1
print(tree.predict({'A' : 1, 'B' : 10})) # 1
print(tree.predict({'A' : 3, 'B' : 11})) # 2
print(tree.predict({'A' : 3, 'B' : 9})) # 3
