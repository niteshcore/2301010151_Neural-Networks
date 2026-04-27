import numpy as np

class Hopfield:
    def __init__(self, size):
        self.size = size
        self.W = np.zeros((size, size))

    def train(self, patterns):
        for p in patterns:
            p = p.reshape(-1,1)
            self.W += p @ p.T
        np.fill_diagonal(self.W, 0)

    def predict(self, s, steps=5):
        s = s.copy()
        for _ in range(steps):
            s = np.sign(self.W @ s)
            s[s==0] = 1
        return s

# Train
patterns = np.array([[1,-1,1],[-1,1,-1]])
hop = Hopfield(3)
hop.train(patterns)

# Test
test = np.array([1,-1,1])
print("Recovered:", hop.predict(test))