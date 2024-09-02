# -*- coding: utf-8 -*-
"""Titanic Survival Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DyzbqRiWYi-znRgmojMzINKP9X3O1wOB

# **🚢 Titanic Survival Prediction Project**
## **Overview**
Welcome to the Titanic Survival Prediction project! 🌊 This project aims to predict the likelihood of survival of passengers on the Titanic using various machine learning models. By analyzing different features such as passenger class, gender, age, and more, we seek to understand the factors that influenced survival rates during this historic disaster.

## **Dataset Description**
The dataset used in this project is derived from the Titanic passenger list. It includes the following key features:

**PassengerId:** A unique identifier for each passenger.

**Survived:** The target variable, where 1 indicates the passenger survived, and 0 indicates they did not.

**Pclass:** The class of the passenger (1st, 2nd, or 3rd).

**Name:** The full name of the passenger.

**Sex:** Gender of the passenger.

**Age:** Age of the passenger.

**SibSp:** Number of siblings or spouses aboard the Titanic.

**Parch:** Number of parents or children aboard the Titanic.

**Ticket:** The ticket number.

**Fare:** The fare paid by the passenger.

**Cabin:** The cabin number.

**Embarked:** The port where the passenger boarded the Titanic.
Project Steps

## **import Relevant Libraries**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""## **Load Datastes**"""

raw_data = pd.read_csv("Titanic-Dataset.csv")

"""## **EDA**"""

df = raw_data.copy()
df.head()

df.info()

df.describe()

df.isnull().sum()

df['Age'] = df['Age'].fillna(df['Age'].mean())

df.isnull().sum()

df['Embarked']= df['Embarked'].fillna(df['Embarked'].mode()[0])

df.isnull().sum()

df['Cabin'].fillna(0,inplace=True)

df.isnull().sum()

# Create a pivot table
pivot_table = df.pivot_table(index='Sex', columns='Survived', aggfunc='size', fill_value=0)
# Plot the data
pivot_table.plot(kind='bar', stacked=True, color=['red', 'green'])
plt.title('Survival Count by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.legend(title='Survived', labels=['Did not survive', 'Survived'])
plt.show()

# Plot the histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='Survived', multiple='stack', palette='Set1', bins=20)
plt.title('Age Distribution by Survival Status')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(title='Survived', labels=['Did not survive', 'Survived'])
plt.show()

sns.histplot(data = df, x= df['Parch'],hue='Survived',multiple='stack', palette='Set1')
plt.show()

sns.countplot(data=df,x=df['Embarked'])
plt.show()

sns.countplot(data=df,x=df['Pclass'])
plt.show()

sns.countplot(data=df,x=df['SibSp'])
plt.show()

df1=df.copy()

## Preprocessing

df1 = df1.drop(columns = ['PassengerId','Name','Ticket','Cabin'],axis=1)

df1



"""## **Data Preprocessing**"""

from sklearn.preprocessing import OrdinalEncoder

cols = ['Sex', 'Embarked']
oe = OrdinalEncoder()
df1[cols] = oe.fit_transform(df1[cols])

X=df1.drop(columns=['Survived'])
y=df1['Survived']



"""## **Feature Selection**"""

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test= train_test_split(X,y,test_size = 0.2,random_state=42 )

X_train.shape,X_test.shape



"""## **Model And Accuracy**"""

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.fit_transform(X_test)

from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

models = [
     LogisticRegression(random_state = 50),
     RandomForestClassifier(),
     DecisionTreeClassifier(random_state=42),
     AdaBoostClassifier(),
     GradientBoostingClassifier(random_state= 42),
     SVC(random_state = 42),
     GaussianNB()
]


for i,model in enumerate(models):
  model.fit(X_train,y_train)
  train_accuracy = accuracy_score(y_train,model.predict(X_train))
  test_accuracy = accuracy_score(y_test,model.predict(X_test))
  print(f"Model {i+1}: {type(model).__name__}")
  print(f"Train accuracy:{train_accuracy}")
  print(f"Test accuracy {test_accuracy}:.2f")
  print("_"*50)

