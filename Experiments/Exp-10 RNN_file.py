import numpy as np
X = np.array([[1,2,3],[2,3,4]])
y = np.sum(X, axis=1)

print("Input:\n", X)
print("Output (sum):", y)