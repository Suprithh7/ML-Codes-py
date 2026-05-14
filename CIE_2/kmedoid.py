import math
import pandas as pd
import random

# Load dataset
df = pd.read_csv('kmedoids.csv')

# Convert dataframe to list
data = df.values.tolist()

k = 2

# Initialize medoids randomly
medoids = random.sample(data, k)

# Distance function
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

while True:

    clusters = [[] for _ in range(k)]

    # Assign points to nearest medoid
    for point in data:

        dists = [distance(point, m) for m in medoids]

        idx = dists.index(min(dists))

        clusters[idx].append(point)

    # Find new medoids
    new_medoids = []

    for cluster in clusters:

        min_cost = float('inf')
        best_medoid = None

        for p1 in cluster:

            cost = 0

            for p2 in cluster:
                cost += distance(p1, p2)

            if cost < min_cost:
                min_cost = cost
                best_medoid = p1

        new_medoids.append(best_medoid)

    # Stop if medoids do not change
    if new_medoids == medoids:
        break

    medoids = new_medoids

# Output
print("Final Medoids:", medoids)

for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: {cluster}")