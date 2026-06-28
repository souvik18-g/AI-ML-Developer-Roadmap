# import means bring code/library from somewhere else

# sklearn = machine learning library
# datasets = ready-made datasets module
# load_iris = function that gives Iris flower dataset
from sklearn.datasets import load_iris


# model_selection = tools related to train/test splitting
# train_test_split = function to split data
from sklearn.model_selection import train_test_split


# tree = module containing tree algorithms
# DecisionTreeClassifier = ML algorithm/class
from sklearn.tree import DecisionTreeClassifier


# import whole joblib library
# used for save/load model files
import joblib


# ---------------- LOAD DATASET ----------------

# iris variable stores whole dataset object
iris = load_iris()

# iris contains:
# data = input features
# target = output labels
# feature names
# target names


# X usually means input/features in ML
# iris.data =
# 150 rows of flower measurements
#
# each row has:
# sepal length
# sepal width
# petal length
# petal width
X = iris.data


# y usually means output/target in ML
# iris.target =
# flower category number
#
# 0 = setosa
# 1 = versicolor
# 2 = virginica
y = iris.target


# ---------------- SPLIT DATA ----------------

# split dataset into:
# training data
# testing data

# X_train = training inputs
# X_test = testing inputs

# y_train = training outputs
# y_test = testing outputs

X_train, X_test, y_train, y_test = train_test_split(

    # X = input data
    X,

    # y = output labels
    y,

    # test_size=0.2
    # 20% data goes for testing
    # 80% goes for training
    test_size=0.2,

    # random_state=42
    # fixed random split
    # same output every run
    random_state=42
)


# ---------------- CREATE MODEL ----------------

# model variable stores ML model object

# DecisionTreeClassifier()
# creates decision tree algorithm

model = DecisionTreeClassifier()


# ---------------- TRAIN MODEL ----------------

# fit() means train the model

# model learns relation between:
# X_train -> inputs
# y_train -> correct answers

model.fit(X_train, y_train)


# ---------------- CHECK ACCURACY ----------------

# score() checks accuracy on test data

# X_test = unseen inputs
# y_test = real answers

# output example:
# 1.0 means 100% accuracy

accuracy = model.score(X_test, y_test)


# print() displays output

# "Accuracy:" = text
# accuracy = variable value

print("Accuracy:", accuracy)


# ---------------- SAVE MODEL ----------------

# joblib.dump()

# dump means save object into file

# model = object to save
# "iris_model.pkl" = filename

# .pkl = pickle file
# stores trained model permanently

joblib.dump(model, "iris_model.pkl")


# print success message
print("Model saved successfully")


# ---------------- LOAD MODEL ----------------

# load() reads saved file back into Python

# loaded_model variable now contains trained model again

loaded_model = joblib.load("iris_model.pkl")


# print success message
print("Model loaded successfully")


# ---------------- PREDICT ----------------

# predict() gives prediction for new data

# [[5.1, 3.5, 1.4, 0.2]]
#
# outer [] = dataset
# inner [] = one flower sample
#
# values mean:
# sepal length
# sepal width
# petal length
# petal width

prediction = loaded_model.predict([[5.1, 3.5, 1.4, 0.2]])


# output example:
# [0]
#
# meaning:
# predicted flower class = 0

print("Prediction:", prediction)