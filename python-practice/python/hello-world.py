# from sklearn import tree
# features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# labels = [0, 0, 1, 1]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features, labels)
# print (clf.predict([[180, 0]]))

import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
test_idx = [0, 50, 100]

train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print (test_target)
print (clf.predict(test_data))
print (test_data[1], test_target[1])
print (iris.feature_names, iris.target_names)
