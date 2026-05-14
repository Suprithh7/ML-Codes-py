import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv('randomforest.csv')

# Features
X = df.iloc[:, :-1]

# Target
Y = df.iloc[:, -1]

# Create Random Forest model
model = RandomForestClassifier(n_estimators=10)

# Train model
model.fit(X, Y)

# Prediction
predictions = model.predict(X)

# Output
print("Predictions:\n")

actual = Y.tolist()
for i in range(len(predictions)):
    print(f"Actual: {actual[i]}, Predicted: {predictions[i]}")