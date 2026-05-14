import pandas as pd

# Load dataset
df = pd.read_csv('svm.csv')

# Features
X = df.iloc[:, :-1].values

# Target
Y = df.iloc[:, -1].values

# Initialize weights and bias
w1 = 0
w2 = 0
b = 0

learning_rate = 0.001
epochs = 1000

# Training
for epoch in range(epochs):

    for i in range(len(X)):

        x1 = X[i][0]
        x2 = X[i][1]

        y = Y[i]

        # Equation
        condition = y * ((w1 * x1) + (w2 * x2) + b)

        if condition >= 1:

            w1 = w1 - learning_rate * (2 * w1)
            w2 = w2 - learning_rate * (2 * w2)

        else:

            w1 = w1 - learning_rate * (2 * w1 - y * x1)
            w2 = w2 - learning_rate * (2 * w2 - y * x2)
            b = b - learning_rate * (-y)

# Output
print("Weight 1 =", w1)
print("Weight 2 =", w2)
print("Bias =", b)

print("\nPredictions:\n")

for i in range(len(X)):

    x1 = X[i][0]
    x2 = X[i][1]

    value = (w1 * x1) + (w2 * x2) + b

    if value >= 0:
        print(X[i], "-> 1")
    else:
        print(X[i], "-> -1")