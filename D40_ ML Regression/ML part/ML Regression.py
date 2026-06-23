from sklearn.linear_model import LinearRegression
import numpy as np

# input
X = np.array([[1],[2],[3],[4],[5]])

# output
Y = np.array([2,4,6,8,10])

# create model
model = LinearRegression()

# train model
model.fit(X, Y)

# score
score = model.score(X, Y)

print("R2 Score:", score)

# prediction
prediction = model.predict([[6],[7]])
print("Prediction:", prediction[0],prediction[1])