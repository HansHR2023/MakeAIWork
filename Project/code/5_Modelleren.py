#!/usr/bin/env python
# coding: utf-8

# <div>
#     <em><h1>Health Marketing</h1></em>
#     <img width="10%" height="10%" src='pics/aiHealth_01.jpg'/>
#     
#     
# </div>
# <div>
#     <p>
#     <em>Stap 5:</em>
#     <br>
#     <em>Data interpretatie: modelleren</em>
#         <br>
#     <em>Author: Hans Olthoff</em>
#     </p>    
# </div>

# In[ ]:


import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)

from sklearn import linear_model 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math


# Get data
# 
# In the db are 3 tables: df1, df2, df3
# 
# - df1 is the complete set (NaNs replaced by mean value)
# - df2 has extra colum BMI
# - df3 has extra colum BMI AND outliers are removed

# In[ ]:


dbConnection = sqlite3.connect('../rest_server_new/medisch_centrum_randstad/db.sqlite3')


# In[ ]:


df = pd.read_sql_query(f"SELECT * FROM {'df2'}", dbConnection)


# In[ ]:


dbConnection.close()


# In[27]:


df = pd.read_csv('data/df2.csv', index_col=0)


# Fit to model

# In[48]:


# Check of index is removed
df.keys()


# In[ ]:





# In[29]:


# divide dataset into X predictors and y target
# X = df.drop(['index', 'lifespan'], axis=1)
X = df.drop(['lifespan'], axis=1)
y = df[['lifespan']]

# split data 80% training and 20% test with random state for reproducability
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[ ]:


# variant waarbij mass en length zijn verwijderd
# divide dataset into X predictors and y target
# X = df.drop(['index', 'mass', 'length', 'lifespan'], axis=1)
# y = df[['lifespan']]

# # split data 80% training and 20% test with random state for reproducability
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[30]:


regr = linear_model.LinearRegression()
regr.fit(X_train, y_train) 


# RSME zegt hoeveel zit het gemiddelde van de lifespan tov wat het model er van maakt. Dus hoe lager de RSME dan is het model beter want een lagere error is een betere voorspelling.
# 
# 
# Mogelijke vervolgstappen zijn:
# - je model testen
# - lse en r squared bekijken
# - decision tree en random forest proberen
# - bovenstaande met de twee andere datsets doorlopen
# 
# 
# 
# 

# In[31]:


# y_test is called p_test, because y_test already exists
p_test = regr.predict(X_test)
 
plt.scatter(y_test,p_test,c='blue', alpha=0.4)
plt.xlabel('True Values')
plt.ylabel('Predictions')
 
# plot diagonal line for comparison (prediction is exact)
lims=[50,110]
plt.xlim(lims)
plt.ylim(lims)
plt.plot(lims,lims,c='black',alpha=0.5)
plt.show()


# In[ ]:





# LSE or Least Square Error to make the error as small as possible. That is what happens with FIT
# The RMSE is the check on the fit.

# In[32]:


score = regr.score(X_test,y_test)
# hier gebruik je de testdata om te checken


# In[33]:


display(score)
# dit geeft R^2 en dat is de accuraatheid van het model


# R^2 or R squared to look at the quality of the fit

# RMSE or Root Mean Squared Error is hoe ver prediction afzit van de werkelijke waarde.
# 

# In[ ]:





# In[34]:


# X_test heeft geen lifespan, dus drop hoeft niet
# X_test.lifespan = y_test


p_test = regr.predict(X_test)
 
mse = mean_squared_error(y_test, p_test)

rmse = (math.sqrt(mse))
print(rmse)


# In[54]:


# y = a1x1 + a2x2 + ... b0 met b0 is de optelsom van alle b waarden

# The coefficients a1, a2, a3, etc
print('Coefficients: \n', regr.coef_)
print(f'b0 would be:',regr.predict([[0,0,0,0,0,0,0,0]]))


# In[52]:


# b0 direct berekenen:
display(regr.intercept_)


# Qua model kan er nog getest worden met andere datasets, zoals gedefinieerd in de vorieg stap.
# 
# Ook kan er getest worden met andere regressie modellen:
# - decision tree
# - random forest
# 
# Ter aanvulling: 
# - clustering toepassen op BMI
# - de lin regressie zelf nabouwen
# 
# Ivm tijdsgebrek zullen bovenstaande opties hier niet nader onderzocht worden.

# In[2]:


#Test met test_invoer: daarvoor neem je de gem waarden. je kan bij invoer ook de min en max aangeven

genetic = 82.28 # min=63.90 max=102.20
length = 183.89 # min = 154.00 max = etc
mass = 92.28
alcohol = 2.27
sugar = 6.49
smoking = 9.81
exercise = 2.40
divider = pow(length/100, 2) if length >0 else None
BMI = round(mass/divider)
logging.debug(f'BMI: {BMI}') 


# In[40]:


df.describe()


# In[43]:


# Test met gemiddelde waarden:

lifespan_predict = regr.predict([[genetic, length, mass, alcohol, sugar, smoking, exercise, BMI]])
display(lifespan_predict)


# In[ ]:





# Twee andere manieren om lifespan_predict te bepalen adhv X_input

# In[ ]:


X_input = [genetic, length, mass, exercise, smoking, alcohol, sugar, BMI]
# dit moet een dict zijn met de {'colum':value, etc}


# In[49]:


#andere manier: X_input bepalen obv de coefficient
# de coeff is de a in y = ax + b en b0 is de optesom van alle individuele b's in y = ax +b
# y = a1x1 + a2x2 +... b0

# lifespan = genetic*1.00 + length*(-0.06) + etc


# In[ ]:





# In[ ]:


# df.keys().drop('index') * regr.coef_[0]


# list(df.keys().drop('index'))
# list(regr.coef_[0])

# (list(df.keys().drop('index')))*(list(regr.coef_[0]))
lifespan =  X_input * list(regr.coef_[0])


# In[ ]:




