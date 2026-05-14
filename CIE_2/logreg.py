import pandas as pd
import math

# Load dataset
df = pd.read_csv('logisticreg.csv')

# Feature and target
X = df.iloc[:, 0].values.tolist()
Y = df.iloc[:, 1].values.tolist()

# Initialize weight and bias
w = 0
b = 0

learning_rate = 0.001
epochs = 1000

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Training
for epoch in range(epochs):

    for i in range(len(X)):

        x = X[i]

        # Linear equation
        z = (w * x) + b

        # Prediction
        y_pred = sigmoid(z)

        # Error
        error = y_pred - Y[i]

        # Update weight and bias
        w = w - learning_rate * error * x
        b = b - learning_rate * error

# Output
print("Weight =", w)
print("Bias =", b)

print("\nPredictions:\n")

for i in range(len(X)):

    z = (w * X[i]) + b

    y_pred = sigmoid(z)

    if y_pred >= 0.5:
        print(X[i], "-> 1")
    else:
        print(X[i], "-> 0")