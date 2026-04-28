import numpy as np
import matplotlib.pyplot as plt  # type: ignore

# Activation Functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def linear(x):
    return x

# Input range
x = np.linspace(-10, 10, 100)

# Plot
plt.plot(x, sigmoid(x), label="Sigmoid")
plt.plot(x, relu(x), label="ReLU")
plt.plot(x, linear(x), label="Linear")

plt.legend()
plt.title("Activation Functions")
plt.xlabel("X")
plt.ylabel("Output")
plt.grid()

plt.show()