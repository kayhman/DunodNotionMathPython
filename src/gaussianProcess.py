import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('grayscale')
from sklearn.gaussian_process.kernels import RBF

X = np.linspace(start=0, stop=10, num=1_000).reshape(-1, 1)
y = np.squeeze(X * np.sin(X))

rng = np.random.RandomState(1)
training_indices = rng.choice(np.arange(y.size), size=6, replace=False)
X_train, y_train = X[training_indices], y[training_indices]
X_test = np.array([x for i, x in enumerate(X)
                           if i not in training_indices])
y_test = np.array([yy for i, yy in enumerate(y)
                   if i not in training_indices])

print(X_train.shape)
#> (6, 1)
print(X_test.shape)
#> (994, 1)

kernel =  1 * RBF(length_scale=1.0)

def predict(kernel, X_train, X_test, y_train):
    K = kernel(X_train, X_train)
    K_star = kernel(X_train, X_test)
    K_double_star = kernel(X_test, X_test)

    y_pred = np.matmul(np.transpose(K_star), np.linalg.inv(K))
    y_pred = np.matmul(y_pred, y_train)
    return y_pred


y_pred_1 = predict(kernel, X_train, X_test, y_train)
plt.plot(X_test[:, 0], y_pred_1, label='Valeurs predites')
plt.plot(X[:, 0], y, label='Valeurs reelles')
plt.scatter(X_train, y_train, label="Points d'entrainement")
plt.legend()
plt.show()
