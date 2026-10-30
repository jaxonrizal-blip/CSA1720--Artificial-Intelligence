from sklearn.neighbors import KNeighborsClassifier

# Training data
X = [[1, 2], [2, 3], [3, 3], [6, 7], [7, 8], [8, 8]]
y = ['A', 'A', 'A', 'B', 'B', 'B']

# Create and train the model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Get user input
x1 = float(input("Enter first feature: "))
x2 = float(input("Enter second feature: "))

# Predict class
prediction = model.predict([[x1, x2]])
print("Predicted class:", prediction[0])
