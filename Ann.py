import math

# Sigmoid activation
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

import pandas as pd

# Load dataset using pandas
df = pd.read_csv('logic_gate_ann.csv')

# Convert dataframe to lists
inputs = df[['x1', 'x2']].values.tolist()
outputs = df['y'].tolist()

# Initialize weights and bias
weights = [0.5, 0.5]
bias = 0.5
learning_rate = 0.1

# Training
for epoch in range(10000): # Increased epochs for better convergence
    for i in range(len(inputs)):
        x = inputs[i]
        target = outputs[i]

        # Forward pass
        net = x[0]*weights[0] + x[1]*weights[1] + bias
        out = sigmoid(net)

        # Error
        error = target - out

        # Backprop (update)
        delta = error * sigmoid_derivative(out)

        weights[0] += learning_rate * delta * x[0]
        weights[1] += learning_rate * delta * x[1]
        bias += learning_rate * delta

# Testing
print("Trained Weights:", weights)
print("Trained Bias:", bias)

for x in inputs:
    net = x[0]*weights[0] + x[1]*weights[1] + bias
    out = sigmoid(net)
    print(f"{x} -> {round(out)} (Actual: {out:.4f})")