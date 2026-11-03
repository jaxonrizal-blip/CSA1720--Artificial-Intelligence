# Import required libraries
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load dataset
data = load_iris()
X = data.data

print("Original Data Shape:", X.shape)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Display reduced data
print("\nReduced Data Shape:", X_pca.shape)
print("\nFirst 5 Reduced Data:")
print(X_pca[:5])

# Display explained variance
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)
