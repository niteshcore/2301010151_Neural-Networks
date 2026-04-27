import numpy as np
from scipy import constants
from scipy.optimize import root, minimize
from scipy.sparse import csr_matrix
from scipy.spatial.distance import euclidean

print("Value of PI:", constants.pi)

def eqn(x):
    return x + np.cos(x)   

sol = root(eqn, 0)
print("Root:", sol.x)

def func(x):
    return x**2 + x + 2

res = minimize(func, 0)
print("Minimum value:", res.fun)
print("At x =", res.x)

arr = np.array([0,0,1,0,2])
mat = csr_matrix(arr)
print("Sparse Matrix:\n", mat)

distance = euclidean((1,0), (10,2))
print("Euclidean Distance:", distance)