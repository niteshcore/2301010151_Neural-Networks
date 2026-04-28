from sklearn.neural_network import MLPClassifier
import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,1,1,0])

model = MLPClassifier(
    hidden_layer_sizes=(4,), 
    max_iter=5000,
    solver='adam',            
    random_state=1
)
model.fit(X, y)
pred = model.predict(X)
print("Predictions:", pred)