# -*- coding: utf-8 -*-
"""LVADSUSR195_Venkatsundhar-SP_LAB-1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19e5MRUKbk7LONXPSmoEsqoDsv07iu2TQ

4403 LAB-1 LINEAR REGRESSION FOR EXPENSES DATASET
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder,MinMaxScaler,StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

df = pd.read_csv('/content/sample_data/expenses.csv')

df.info()

df.describe()

"""TASK:1 - Handling missing values and outliers"""

#1a
df.isnull().sum()

# There are 16 null values in the dataset
# Which is 1 % of dataset and is insignificant.
# Dropping it wont affect the dataset
16/1338

# Drop null
df.dropna(inplace=True)

#1b To manage outliers using boxplots
df_num = df.select_dtypes(include=['int64','float64'])
cols = df_num.columns
for c in cols:
  plt.figure(figsize=(10,7))
  sns.boxplot(df[c])
  plt.title(f"Box plot showing {c}")

# There are outliers in charges and bmi columns as identified from boxplots

"""TASK-2 ENCODING CATEGORICAL DATA"""

#2a
df_cat = df.select_dtypes(include=['object'])
col_cat = df_cat.columns
L = LabelEncoder()
for c in col_cat:
  df[c]=L.fit_transform(df[c])
df #After label encoding

df['region'].unique()

'''
sex is categorized as 0 & 1
smoker / non smoker is categorized as 0 & 1
Region is also categorized as 0,1,2 & 3
'''

"""TASK-3 FEATURE SELECTION AND DATA CLEANING"""

#3a
# Relevance can be found out by using scatter plots / correlation matrix / heatmap

# Scatter plots for numerical data (including categorical which is encoded)
# Scatter plot
df_num = df.select_dtypes(include=['int64','float64'])
cols = df_num.columns
for i in range(len(cols)):
  for j in range(i+1,len(cols)):
    plt.figure(figsize=(9,6))
    plt.scatter(data=df_num,x=cols[i],y=cols[j])
    plt.title(f"Scatter plot {cols[i]} vs {cols[j]}")

# Age & Charges, Bmi & charges seem to have some correlation as the graph tends to move linearly

# Correlation test
corr = df_num.corr()
sns.heatmap(corr,annot=True,fmt='.2f')

'''
Correlation matrix shows there is only significane relation between
smoking and charges
When the person is a smoker his insurance charges tend to increase
'''

'''
Rest considering we should use all features as there
is no significance correlation between variables to drop
'''

#3b
df.duplicated().sum()

df.drop_duplicates(inplace=True)

df.duplicated().sum()

# Duplicates have been dropped

"""TASK-4 DATASET SPLITTING"""

df.columns

#4
X = df[['age', 'sex', 'bmi', 'children', 'smoker', 'region']]
y = df['charges']
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=101)
# 20% data is used for TESTING

# Scaling the variables
Scaler = MinMaxScaler()
X_train = Scaler.fit_transform(X_train)
X_test = Scaler.transform(X_test)

"""TASK-5 MODEL DEVELOPMENT AND TRAINING"""

#5a
LR = LinearRegression()
LR.fit(X_train,y_train)

"""TASK-6 MODEL EVALUATION"""

#6
#Scaler
predicted = LR.predict(X_test)
MSE = mean_squared_error(y_test,predicted)
print("MSE:",MSE)
RMSE = np.sqrt(mean_squared_error(y_test,predicted))
print("RMSE:",RMSE)
r2 = r2_score(y_test,predicted)
print("R2_score:",r2)
