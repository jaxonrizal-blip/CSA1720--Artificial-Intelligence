from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([20, 30, 40, 50, 60])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Get user input
hours = float(input("Enter hours studied: "))

# Predict marks
prediction = model.predict([[hours]])

print("Predicted marks:", prediction[0])
