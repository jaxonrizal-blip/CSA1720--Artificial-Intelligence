from sklearn.tree import DecisionTreeClassifier

# Training data: [Hours studied, Attendance]
X = [[2, 60], [3, 65], [4, 70], [6, 80], [7, 85], [8, 90]]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Get user input
hours = float(input("Enter hours studied: "))
attendance = float(input("Enter attendance percentage: "))

# Predict result
prediction = model.predict([[hours, attendance]])

if prediction[0] == 1:
    print("Predicted Result: Pass")
else:
    print("Predicted Result: Fail")
