# -*- coding: utf-8 -*-
"""using xg_boost.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j9g3TBYTepnwPJ39MnSv0t3ccbMAfl1y
"""

###importing the drive

from google.colab import drive
drive.mount('/content/drive')

"""Process values from CellProfiler.exe
As of the duration of this project, Cellprofier wasnt available as an importable library for either Google colab/Jupyter Notebook, as in installable library
"""

import pandas as pd
df = pd.read_csv("/content/drive/My Drive/50 img/final merge end viva.csv")
df.tail()
df.drop('Threshold_GuideThreshold_Threshold',axis=1,inplace=True)

label=pd.read_csv("/content/drive/My Drive/50 img/final merge 2.csv")
label.tail()

"""final merge end viva- params

final merge 2- results
"""

label.value_counts()

###Separting features and labels

df.shape

# x, y = df.iloc[:, :-1], df.iloc[:, [-1]]
x = df
x.tail()

y = label
y.tail()

#converting csv to matrix for features
feature_matrix = x.values
print(feature_matrix)



#converting csv to matrix for training data
result_matrix = y.values
# print(result_matrix)


result_matrix

#traning the model

import xgboost as xgb

# model = xgb.XGBClassifier(objective="binary:logistic")
#depth, subsample found best found best. learning has been set to 1 as referred to paper, rest bruteforced
model = xgb.XGBClassifier(objective="binary:logistic", booster="gbtree", subsample= 0.85, tree_method="exact", max_depth= 3, learning_rate=1)

model.fit(feature_matrix,result_matrix)

# for i in range(0,101):
#   print("for random state ")
#   print(i)
#   model = xgb.XGBClassifier(objective="binary:logistic",random_state=i)
#   model.fit(feature_matrix,result_matrix)
#   pred = model.predict(feature_matrix)
#   from sklearn.metrics import accuracy_score
#   score = accuracy_score(result_matrix,pred)*100
#   print (score)

pred = model.predict(feature_matrix)

pred

from sklearn.metrics import confusion_matrix
mat = confusion_matrix(result_matrix,pred)
mat

from sklearn.metrics import accuracy_score
accuracy_score(result_matrix,pred)*100

import numpy as np
sum = np.sum(mat)
print(sum)

np.unique(pred)



