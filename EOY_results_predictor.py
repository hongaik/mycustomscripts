import os
import pandas as pd
import numpy as np
from glob import glob
from scipy import stats
from sklearn import linear_model
import seaborn as sns
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
os.chdir('C:\\Users\\jeryl\\desktop\\python\\results predictor')
col_names = ['CT1', 'CT2', 'MYE', 'CT3', 'EYE']

df_list=[]
for file in glob('F1*.csv'):
    df = pd.read_csv(file)
    df = df.iloc[6:47,[9,12,18,24,30]]
    df.columns = col_names
    df_list.append(df)

#Data cleaning
df = pd.concat(df_list)
df = df.reset_index()
df = df.drop(['index'], axis=1)
df.replace('#VALUE!', np.nan, inplace=True)
df.replace('VR', np.nan, inplace=True)
df.replace('vr', np.nan, inplace=True)
df.replace('MC', np.nan, inplace=True)
df.replace('No. of', np.nan, inplace=True)
df = df.dropna()
df[col_names] = df[col_names].apply(pd.to_numeric)

#Feature engineering
df['AVG'] = (df['CT1']+df['CT2']+df['CT3']+df['MYE'])/4

trng_data = df[['AVG']]
labels = df['EYE']

#Fitting linear model
reg_all = linear_model.LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(trng_data, labels,
                                                    test_size = 0.3, random_state=42)
reg_all.fit(X_train, y_train)
y_pred = reg_all.predict(X_test)
print('MSE: '+str(mean_squared_error(y_test, y_pred)))
print(reg_all.coef_, reg_all.intercept_)

#Visualising prediction results
plt.figure()
plt.xlim(0,100)
plt.ylim(0,100)
plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")
plt.scatter(y_test, y_pred)
plt.plot([0,50,100], [0,50,100], color='r')
plt.show()

