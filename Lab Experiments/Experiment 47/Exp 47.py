from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Dataset Loaded Successfully!")
print("Total Samples:", len(X))

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create Model
model = RandomForestClassifier(random_state=42)

# Define Hyperparameters
parameter_grid = {
    "n_estimators": [50, 100],
    "max_depth": [3, 5, None],
    "min_samples_split": [2, 5]
}

# Hyperparameter Tuning
grid_search = GridSearchCV(
    estimator=model,
    param_grid=parameter_grid,
    cv=3,
    scoring="accuracy",
    n_jobs=1
)

print("\nStarting Hyperparameter Tuning...")
grid_search.fit(X_train, y_train)

# Display Results
print("\nHyperparameter Tuning Completed!")

print("\nBest Parameters:")
print(grid_search.best_params_)

print("\nBest Cross Validation Accuracy:")
print(grid_search.best_score_)

# Best Model
best_model = grid_search.best_estimator_

# Prediction
y_pred = best_model.predict(X_test)

# Evaluation
print("\nTest Accuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
