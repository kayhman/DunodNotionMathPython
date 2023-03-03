    class DecisionNode:
    """
    Node decision class.
    This is a simple binary node, with potentially two children: left and right
    Left node is returned when condition is true
    False node is returned when condition is false
    """
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
        """
        Node is a leaf if it has no child
        """
        return (not self.left) and (not self.right)

    def next(self, data):
        """
        Return next node depending on data and node condition
        """
        cond = self.condition(data)
        if cond:
            return self.left
        else:
            return self.right


class DecisionTree:
    """
    A DecisionTree is a model that provides predictions depending on input.
    A Prediction is the sum of the leaves' values, for those leaves that were activated by the input
    """
    def __init__(self, root):
        """
        A DecisionTree is defined by an objective, a number of estimators and a max depth.
        """
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
