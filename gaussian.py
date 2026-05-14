import math
import pandas as pd

# Load dataset using pandas
df = pd.read_csv('iris.csv')

# Convert dataframe to the format: [feature1, feature2, ..., class]
data = df.values.tolist()

# Separate data by class
classes = {}
for row in data:
    label = row[-1]
    if label not in classes:
        classes[label] = []
    classes[label].append(row[:-1])

# Mean
def mean(numbers):
    return sum(numbers) / len(numbers)

# Variance
def variance(numbers, m):
    if len(numbers) <= 1: return 0.0001 # Avoid division by zero or zero variance
    return sum((x - m) ** 2 for x in numbers) / len(numbers)

# Gaussian probability
def gaussian(x, m, v):
    if v == 0: v = 0.0001 # Avoid division by zero
    exponent = math.exp(-((x - m) ** 2) / (2 * v))
    return (1 / math.sqrt(2 * math.pi * v)) * exponent

# Train: calculate mean & variance
summary = {}
for label, rows in classes.items():
    summary[label] = []
    for i in range(len(rows[0])):
        col = [row[i] for row in rows]
        m = mean(col)
        
        v = variance(col, m)
        summary[label].append((m, v))

# Predict
def predict(input_data):
    probs = {}
    total_rows = len(data)

    for label, stats in summary.items():
        probs[label] = len(classes[label]) / total_rows  # prior

        for i in range(len(stats)):
            m, v = stats[i]
            probs[label] *= gaussian(input_data[i], m, v)

    return max(probs, key=probs.get)

# Test with an example from each class
test_setosa = [5.1, 3.5, 1.4, 0.2]
print("Predicted class for setosa sample:", predict(test_setosa))

test_versicolor = [6.7, 3.1, 4.4, 1.4]
print("Predicted class for versicolor sample:", predict(test_versicolor))

test_virginica = [6.3, 3.3, 6.0, 2.5]
print("Predicted class for virginica sample:", predict(test_virginica))