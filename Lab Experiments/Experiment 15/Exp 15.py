
from sklearn.tree import DecisionTreeClassifier

# Training data
X = [[1], [2], [3], [4], [5], [6]]
y = ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass"]

model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

hours = float(input("Enter study hours: "))

prediction = model.predict([[hours]])

print("Prediction:", prediction[0])
