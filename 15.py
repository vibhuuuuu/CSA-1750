# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# Load the Iris dataset
iris = load_iris()

# Split the dataset into features (X) and target labels (y)
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a DecisionTreeClassifier model
clf = DecisionTreeClassifier()

# Train the model using the training data
clf.fit(X_train, y_train)

# Make predictions using the testing data
y_pred = clf.predict(X_test)

# Calculate accuracy of the model
accuracy = metrics.accuracy_score(y_test, y_pred)

# Print the accuracy
print(f"Accuracy: {accuracy * 100:.2f}%")

# Optional: Visualize the decision tree
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()
