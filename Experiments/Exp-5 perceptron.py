import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

w = np.zeros(2)
lr = 0.1

for _ in range(10):
    for i in range(len(X)):
        pred = 1 if np.dot(X[i], w) > 0 else 0
        w += lr * (y[i] - pred) * X[i]

print("Weights:", w)