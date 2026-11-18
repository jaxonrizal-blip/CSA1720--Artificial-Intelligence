import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Create sample dataset
X, y = make_blobs(
    n_samples=200,
    centers=3,
    cluster_std=1.0,
    random_state=42
)

# Step 2: Convert data into DataFrame
df = pd.DataFrame(X, columns=["Feature 1", "Feature 2"])

print("Sample Dataset:")
print(df.head())

# Step 3: Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Step 4: Apply K-Means clustering
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

# Step 5: Display cluster results
print("\nCluster Results:")
print(df.head(10))

# Step 6: Display cluster centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# Step 7: Visualize clusters
plt.figure(figsize=(8, 5))

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=df["Cluster"],
    cmap="viridis",
    s=50
)

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    color="red",
    marker="X",
    s=200,
    label="Centroids"
)

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

print("\nK-Means Clustering Completed Successfully!")
