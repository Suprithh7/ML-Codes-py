# Gradient Descent for Linear Regression
# Lab Ready Program

import pandas as pd

# Load dataset
data = pd.read_csv("gradient.csv")

# Input and Output
x = data['x']
y = data['y']

# Initialize parameters
m = 0   # slope
b = 0   # intercept

# Learning rate and iterations
L = 0.001
epochs = 1000

n = len(x)

# Gradient Descent
for i in range(epochs):

    dm = 0
    db = 0

    for j in range(n):

        y_pred = m * x[j] + b

        dm += (-2/n) * x[j] * (y[j] - y_pred)
        db += (-2/n) * (y[j] - y_pred)

    # Update parameters
    m = m - L * dm
    b = b - L * db

# Final equation
print("Slope (m) =", m)
print("Intercept (b) =", b)

# Predictions
print("\nPredicted Values:")

for i in range(n):
    pred = m * x[i] + b
    print("x =", x[i], " Predicted y =", round(pred,2))