
#  ML TASK
# Compare 3 ML Models




# Import Dataset


from sklearn.datasets import load_iris



# Import train_test_split


from sklearn.model_selection import train_test_split



# Import Models


from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.linear_model import LogisticRegression



# Load Iris Dataset


iris = load_iris()

# Features
X = iris.data

# Target labels
y = iris.target



# Split Dataset
# 80% Train
# 20% Test


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# Decision Tree Model


dt_model = DecisionTreeClassifier()

# Train model
dt_model.fit(X_train, y_train)

# Check accuracy
dt_score = dt_model.score(X_test, y_test)



# Random Forest Model


rf_model = RandomForestClassifier()

# Train model
rf_model.fit(X_train, y_train)

# Check accuracy
rf_score = rf_model.score(X_test, y_test)



# Logistic Regression Model


lr_model = LogisticRegression(max_iter=200)

# Train model
lr_model.fit(X_train, y_train)

# Check accuracy
lr_score = lr_model.score(X_test, y_test)



# Print Results


print("Decision Tree Accuracy:")
print(dt_score)

print("\nRandom Forest Accuracy:")
print(rf_score)

print("\nLogistic Regression Accuracy:")
print(lr_score)