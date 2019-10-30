import numpy as np
from sklearn import preprocessing,  neighbors, model_selection, svm
from sklearn.model_selection import cross_validate
import pandas as pd


## Select outlier for '?' 
df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)


# X is features and y is labels/class

X = np.array(df.drop(['class'],1))
y = np.array(df['class'])

#  Create training and testing samples from Sci-kit learn
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2)

# Defining the classifier
clf = svm.SVC()

# Train the classifier 
clf.fit(X_train, y_train)

# Testing the classifier
accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures = np.array([4,2,1,1,1,2,3,2,1])
example_measures = example_measures.reshape(1, -1)

prediction = clf.predict(example_measures)
print(prediction)
