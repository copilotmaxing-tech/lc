
import numpy as np

X = np.array([
    [1, 45, 35],
    [3, 60, 50],
    [5, 75, 65],
    [7, 90, 85],
    [9, 95, 94]
], dtype=float)

y = np.array([[0], [0], [1], [1], [1]])

# Normalize input
X = X / np.max(X, axis=0)

# Initialize weights and bias
w = np.zeros((3, 1))
b = 0
lr = 0.5

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Training
for i in range(5000):

    # Forward propagation
    output = sigmoid(np.dot(X, w) + b)

    # Calculate error
    error = y - output

    # Backpropagation
    delta = error * output * (1 - output)

    # Update weights and bias
    w += lr * np.dot(X.T, delta)
    b += lr * np.sum(delta)

# Prediction
output = sigmoid(np.dot(X, w) + b)

print("Actual Output:", y.flatten())
print("Predicted Output:", (output >= 0.5).astype(int).flatten())
