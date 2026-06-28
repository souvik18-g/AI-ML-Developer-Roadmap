from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
iris = load_iris()

# Features
X = iris.data

# Labels
Y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)

print(accuracy)