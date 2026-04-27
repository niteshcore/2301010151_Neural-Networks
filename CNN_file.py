import numpy as np

image = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

kernel = np.array([
    [1,0],
    [0,-1]
])

result = np.zeros((2,2))

for i in range(2):
    for j in range(2):
        result[i,j] = np.sum(image[i:i+2, j:j+2] * kernel)

print("Convolution Output:\n", result)