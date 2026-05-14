import math

import pandas as pd

# Load dataset using pandas
df = pd.read_csv('cluster_data.csv')

# Convert dataframe to the format: [feature1, feature2]
data = df.values.tolist()

k = 3  # Increased k for cluster_data.csv

# Initialize centroids (random points from data)
import random
centroids = random.sample(data, k)

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

while True:
    clusters = [[] for _ in range(k)]

    # Assign points to nearest centroid
    for point in data:
        dists = [distance(point, c) for c in centroids]
        idx = dists.index(min(dists))
        clusters[idx].append(point)

    # Compute new centroids
    new_centroids = []
    for cluster in clusters:
        if cluster:
            x_mean = sum(p[0] for p in cluster) / len(cluster)
            y_mean = sum(p[1] for p in cluster) / len(cluster)
            new_centroids.append([x_mean, y_mean])
        else:
            # Re-initialize if cluster is empty (unlikely with this data)
            new_centroids.append([0, 0])

    # Stop if no change
    if new_centroids == centroids:
        break

    centroids = new_centroids

# Output
print("Final Centroids:", centroids)
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: {cluster}")