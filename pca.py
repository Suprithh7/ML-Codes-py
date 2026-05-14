import pandas as pd
from sklearn.decomposition import PCA

# Load dataset
df = pd.read_csv('pca.csv')

# Take all columns as features
X = df.values

# Apply PCA
pca = PCA(n_components=2)

principal_components = pca.fit_transform(X)

# Output
print("Principal Components:\n")

for row in principal_components:
    print(row)

print("\nExplained Variance Ratio:\n")
print(pca.explained_variance_ratio_)