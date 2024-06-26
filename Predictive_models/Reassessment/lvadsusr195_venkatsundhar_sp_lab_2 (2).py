# -*- coding: utf-8 -*-
"""LVADSUSR195_Venkatsundhar-SP_LAB-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1myD2tT5vRk_kcXZIg3H56zC0NvgVMdNY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from matplotlib.ticker import MultipleLocator
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,classification_report,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
import warnings
warnings.filterwarnings("ignore")
from matplotlib.ticker import MultipleLocator

df = pd.read_csv('/content/mushroom.csv')
df.head()

df.info()

df.shape

df.describe()

df.isnull().sum()

28/54035

df.dropna(inplace=True)

df.isnull().sum()

df.duplicated().sum()

303/54305

df.drop_duplicates(inplace=True)

df.duplicated().sum()

for c in df.select_dtypes(include=['int64','float64']):
  plt.figure(figsize=(9,5))
  sns.boxplot(df[c])

for c in df.select_dtypes(include=['int64','float64']):
  q1 = df[c].quantile(0.25)
  q3 = df[c].quantile(0.75)
  iqr = q3-q1
  upr = q3+1.5*iqr
  lwr = q1-1.5*iqr
  df.loc[df[c]>upr,c] = upr
  df.loc[df[c]<lwr,c] = lwr
  # Treating outliers using iqr methods by clipping to upper and lower bound
  # Correlation to check the strength of the variables

for c in df.select_dtypes(include=['int64','float64']):
  plt.figure(figsize=(9,5))
  sns.boxplot(df[c])

df.columns

L = LabelEncoder()
df['class'] = L.fit_transform(df[c])

df.head()

df.columns

corr = df[['cap-diameter', 'cap-shape', 'gill-attachment', 'gill-color',
       'stem-height', 'stem-width', 'stem-color', 'season']].corr()
plt.figure(figsize=(12,7))
sns.heatmap(corr,annot=True,fmt='.2f',linewidths=0.5)

df.columns

X = df[['cap-diameter', 'cap-shape', 'gill-attachment', 'gill-color',
       'stem-height', 'stem-width', 'stem-color', 'season']]
y = df['class']
# Selecting suitable features for model

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)

S = MinMaxScaler()
X_train = S.fit_transform(X_train)
X_test = S.transform(X_test)

Rf = RandomForestClassifier(n_estimators=80)
Rf.fit(X_train,y_train)
predicted = Rf.predict(X_test)

# RF Metrics
print("Accuracy_score:",accuracy_score(y_test,predicted))
print("Precision_score:",precision_score(y_test,predicted))
print("Recall_score:",recall_score(y_test,predicted))
print("F1-score:",f1_score(y_test,predicted))
print("Classification_report:\n",classification_report(y_test,predicted))
print("Confusion_matrix:\n",confusion_matrix(y_test,predicted))

