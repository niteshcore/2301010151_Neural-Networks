import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1,2,3],[4,5,6]])

print("1D Array:", a)

print("2D Array:\n", b)

print("Shape:", b.shape)

print("Zeros:\n", np.zeros((2,2)))

print(np.eye(2))

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[:2,1:3])

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print(np.dot(x,y))

print(x.T)

print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))

print(np.random.random((2,2)))

print(x + y)
print(x - y)
print(x * y)
print(x / y)
