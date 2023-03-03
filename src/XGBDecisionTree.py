from asciitree import LeftAligned
from collections import OrderedDict as OD
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from jax import grad, jacfwd, jacrev, jit
import jax.numpy as jnp
import numpy as np
from drawtree import draw_level_order

import random

def hessian(fun):
  return jit(jacfwd(jacrev(fun)))

class DecisionNode:
    """
    Node decision class.
    This is a simple binary node, with potentially two childs: left and right
    Left node is returned when condition is true
    False node is returned when condition is false<
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
        Return next code depending on data and node condition
        """
        cond = self.condition(data)
        if cond:
            return self.left
        else:
            return self.right

class DecisionTree:
    """
    A DecisionTree is a model that provides predictions depending on input.
    Prediction is the sum of the values attached to leaf activated by input
    """
    def __init__(self, objective, nb_estimators, max_depth):
        """
        A DecisionTree is defined by an objective, a number of estimators and a max depth.
        """
        self.roots = [DecisionNode(f'root_{esti}', None, 0.0) for esti in range(0, nb_estimators)]
        self.objective = objective
        self.lbda = 0.0
        self.gamma = 1.0 * 0
        self.grad = grad(self.objective)
        self.hessian = hessian(self.objective)
        self.max_depth = max_depth
        self.base_score = None


    def _create_condition(self, col_name, split_value):
        """
        Create a closure that capture split value
        """
        return lambda dta : dta[col_name] < split_value

    def _pick_columns(self, columns):
        return random.choice(columns)

    def _add_child_nodes(self, node, nodes,
                         node_x, node_y,
                         split_value, split_column,
                         nb_nodes,
                         left_w, right_w, prev_w):
        node.name = f'{split_column} < {split_value}'
        node.condition = self._create_condition(split_column, split_value) # we must create a closure to capture split\_value copy
        node.add_left_node(DecisionNode(f'left_{nb_nodes} - {split_column} < {split_value}',
                                        None, left_w + prev_w))
        node.add_right_node(DecisionNode(f'right_{nb_nodes} - {split_column} >= {split_value}',
                                         None, right_w + prev_w))
        mask = node_x[split_column] < split_value
        # Reverse order to ensure bfs
        nodes.append((node.left,
                      node_x[mask].copy(),
                      node_y[mask].copy(),
                      left_w + prev_w))
        nodes.append((node.right,
                      node_x[~mask].copy(),
                      node_y[~mask].copy(),
                      right_w + prev_w))


    def fit(self, x_train, y_train):
        """
        Fit decision trees using x_train and objective
        """
        self.base_score = y_train.mean()
        for tree_idx, tree_root in enumerate(self.roots):
            # store current node (currenly a lead), x\_train and node leaf weight
            nodes = [(tree_root, x_train.copy(), y_train.copy(), 0.0)]
            nb_nodes = 0
            # Add node to tree using bfs
            while nodes:
                node, node_x, node_y, prev_w = nodes.pop(0)
                node_x['pred'] = self.predict(node_x)
                split_column = self._pick_columns(x_train.columns) # XGBoost use a smarter heuristic here
                best_split, split_value, left_w, right_w = self._find_best_split(split_column,
                                                                                 node_x, node_y)
                if best_split != -1:
                    self._add_child_nodes(node, nodes,
                                          node_x, node_y,
                                          split_value, split_column,
                                          nb_nodes,
                                          left_w, right_w, prev_w)
                nb_nodes += 1
                if nb_nodes >= 2**self.max_depth-1:
                    break


    def _gain_and_weight(self, x_train, y_train):
        """
        Compute gain and leaf weight using automatic differentiation
        """
        pred = x_train['pred'].values
        G_i = self.grad(pred, y_train.values).sum()
        H_i = self.hessian(pred, y_train.values).sum()
        return -0.5 * G_i * G_i / (H_i + self.lbda) + self.gamma, -G_i / (H_i + self.lbda)

    def _find_best_split(self, col_name, node_x, node_y):
        """
        Compute best split
        """
        x_sorted = node_x.sort_values(by=col_name)
        y_sorted = node_y[x_sorted.index]
        current_gain, _ = self._gain_and_weight(x_sorted, node_y)
        gain = 0.0
        best_split = -1
        split_value, best_left_w, best_right_w = None, None, None
        for split_idx in range(1, x_sorted.shape[0]):
            left_data = x_sorted.iloc[:split_idx]
            right_data = x_sorted.iloc[split_idx:]
            left_y = y_sorted.iloc[:split_idx]
            right_y = y_sorted.iloc[split_idx:]
            left_gain, left_w = self._gain_and_weight(left_data, left_y)
            right_gain, right_w = self._gain_and_weight(right_data, right_y)
            if current_gain - (left_gain + right_gain) > gain:
                gain = current_gain - (left_gain + right_gain)
                best_split = split_idx
                split_value = x_sorted[col_name].iloc[split_idx]
                best_left_w = left_w
                best_right_w = right_w
        return best_split, split_value, best_left_w, best_right_w

    def predict(self, data):
        preds = []
        for _, row in data.iterrows():
            pred = 0.0
            for tree_idx, root in enumerate(self.roots):
                child = root
                while child and not child.is_leaf():
                    child = child.next(row)
                pred += child.value
            preds.append(pred)
        return np.array(preds) + self.base_score

    def show(self):
        print('not yet implemented')


def squared_error(y_pred, y_true):
    diff = y_true - y_pred
    return jnp.dot(diff, diff.T)

x_train = pd.DataFrame({"A" : [3.0, 2.0, 1.0, 4.0, 5.0, 6.0, 7.0]})
y_train = pd.DataFrame({"Y" : [3.0, 2.0, 1.0, 4.0, 5.0, 6.0, 7.0]})

tree = DecisionTree(squared_error, 1, 3)
tree.fit(x_train, y_train['Y'])
pred = tree.predict(pd.DataFrame({'A': [1., 2., 3., 4., 5., 6., 7.]}))
print(pred) #-> [1. 2. 3. 4. 5. 6. 7.]

tree = DecisionTree(squared_error, 2, 3)
tree.fit(x_train, y_train['Y'])
pred = tree.predict(pd.DataFrame({'A': [1., 2., 3., 4., 5., 6., 7.]}))
print(pred) #-> [1. 2. 3. 4. 5. 6. 7.]

tree = DecisionTree(squared_error, 4, 2)
tree.fit(x_train, y_train['Y'])
pred = tree.predict(pd.DataFrame({'A': [1., 2., 3., 4., 5., 6., 7.]}))
print(pred) # -> [1.        2.        3.        4.        5.        5.9999995 7.       ]

x_train = pd.DataFrame({'A': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0,
                              1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0,],
                        'B': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                              1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,]})
y_train = pd.DataFrame({"Y" : [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0,
                               1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]})

tree = DecisionTree(squared_error, 1, 6)
tree.fit(x_train, y_train['Y'])
pred = tree.predict(pd.DataFrame({'A': [1., 2., 3., 4., 5., 6., 7.],
                                  'B': [0., 1., 0., 1., 0., 1., 0.]}))
print(pred) #-> [1.  2.5 3.  4.5 5.  6.5 7. ]
