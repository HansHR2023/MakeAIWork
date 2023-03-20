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
#     <em>Stap 4:</em>
#     <br>
#     <em>Data interpretatie: EDA</em>
#         <br>
#     <em>Author: Hans Olthoff</em>
#     </p>    
# </div>

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[10]:


# read cleaned_data_2.csv file
# check on index col and remove if necessary

df = pd.read_csv('data/cleaned_data_2.csv', index_col=0)


# ## Exploratory Data Analysis

# In[9]:


df.head()


# In[5]:


df.tail()


# In[11]:


df.info()


# Look at more characteristics of the data

# In[12]:


df.describe()


# ## Investigation of each variable
# Boxplots and scatterplots: characteristics and outliers
# 

# ### Genetic

# In[13]:


# Boxplot 'genetic'
sns.boxplot(x=df['genetic'])


# In[20]:


# lifespan is the y-variable and the other values are X-values 

y = df['genetic']
x = df['lifespan']

ylabel = plt.ylabel('Genetic age')
xlabel = plt.xlabel('Lifespan in years')

display(plt.scatter(x, y))


# ### Length

# In[18]:


# Boxplot 'length'
sns.boxplot(x=df['length'])


# In[21]:


x = df['length']
y = df['lifespan']

xlabel = plt.xlabel('Length in centimetres')
ylabel = plt.ylabel('Lifespan in years')

display(plt.scatter(x, y))


# ### Mass

# In[22]:


# Boxplot 'mass'
sns.boxplot(x=df['mass'])


# In[26]:


x = df['mass']
y = df['lifespan']

xlabel = plt.xlabel('Body weight in kilograms')
ylabel = plt.ylabel('Lifespan in years')

display(plt.scatter(x, y))


# ### Exercise

# In[27]:


# Boxplot 'exercise'
sns.boxplot(x=df['exercise'])


# In[21]:


# So there may be an exercise-outlier here
overThreeHrsEx = healthData.query("exercise >= 3.0") 
#display(overThreeHrsEx)
amountOverThreeHrsEx = overThreeHrsEx.count()
display(amountOverThreeHrsEx)
# Apparently there are 1288 persons who exercise over 3 hrs per day


# Would it be a good thing to remove these entries from the df? How extreme did these people really sport? Compared to 3 hrs per day, 4 hrs does not sound that extreme to me (like 10 hrs would). What if these 4-hr sporters have a really nice lifespan compared to 'less active sporters' ??
# 

# In[22]:


x = healthData['lifespan']
y = healthData['exercise']
xlabel = plt.xlabel('Lifespan in years')
ylabel = plt.ylabel('Amount of exercise in hours per day')
display(plt.scatter(x, y))


# It does look like those who exercise more hours per day live longer lives. The difference between 3 or 4 hours in relation to lifespan doesn't seem to Ibe that significant. Just wondering: how many of the active people do also smoke? I expect 'low active people' to smoke more sigarettes than those who work out 4 hrs per day. ( I don't expect them to smoke at all.)

# In[23]:


x = healthData['exercise']
y = healthData['smoking']
xlabel = plt.xlabel('Amount of exercise in hours per day')
ylabel = plt.ylabel('Number of cigarettes per day')
display(plt.scatter(x, y))


# I was not expecting this.  
# Apparently, there are heavy smokers in every sporting group.

# ### Smoking

# In[24]:


# Boxplot 'smoking'
sns.boxplot(x=healthData['smoking'])
# No outliers


# In[25]:


x = healthData['lifespan']
y = healthData['smoking']
xlabel = plt.xlabel('Lifespan in years')
ylabel = plt.ylabel('Number of cigarettes per day')
display(plt.scatter(x, y))


# No surprise here really: those who smoke a lot tend to die earlier than those who smoke less or not at all. 

# ### Sugar

# In[26]:


# Boxplot 'sugar'
sns.boxplot(x=healthData['sugar'])


# In[27]:


# So there may be sugar-outliers here
overFourSugar = healthData.query("sugar >= 4") 
#display(overFourSugar)
amountOverFourSugar = overFourSugar.count()
display(amountOverFourSugar)
# Apparently there are 1072 persons who take over 4 lumps of sugar every day


# In[28]:


x = healthData['lifespan']
y = healthData['sugar']
xlabel = plt.xlabel('Lifespan in years')
ylabel = plt.ylabel('Sugar cubes consumed per day')
display(plt.scatter(x, y))


# So it seems people die earlier the more sugar they eat per day.  
# People who eat the equivalent of 5 sugar cubes a day typically do not reach 90 years of age.  
# In the group of people who eat 3 or more sugar cubes a day, mortality starts to occur as early as the mid-40s.  
# While in the group of people who eat 2 sugar cubes or less a day, this does not happen until their (mid) 50s.

# ### Lifespan

# In[29]:


# Boxplot 'lifespan'
sns.boxplot(x=healthData['lifespan'])
# There may be outliers here


# In[30]:


# So there may be lifespan-outliers here (Age limits chosen on sight.)
lifespOutl = healthData.query("lifespan <= 46" and "lifespan >= 104") 
#display(LifespOutl)
amountLifespOutl = lifespOutl.count()
display(amountLifespOutl)
# Apparently in this population there were 64 people '46 or younger' or ' 104 or older' when they died.
print()
negLifespOutl = healthData.query("lifespan <= 46") 
amountNegLifespOutl = negLifespOutl.count()
display(amountNegLifespOutl)
# Apparently in this population there were 9 people '46 or younger' when they died.



# ## Heatmap
# Before deciding whether or not to discard of the outliers I'd like to see the heatmap.
# 

# In[31]:


plt.figure(figsize=(10,5))
c= healthData.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c


# ## First conclusions
# It looks like exercise has a huge positive influence on lifespan, while smoking has a (lesser) negative influence on lifespan.  
# Less important than smoking, but still important: a negative correlation between lifespan and sugarconsumption, alcoholconsumption and mass.  
# It seems that Lifestyle-choices are more important than (given factors like) genetics or length.  
# Nb: 'exercise' and 'sugar', aswell as 'lifespan' seem to have 'outliers'.
# 

# ## New Dataframe without the outliers

# In[32]:


Q1 = healthData.quantile(0.25)
Q3 = healthData.quantile(0.75)
IQR = Q3 - Q1
print(Q1)
print()
print(Q3)
print()
print(IQR)
healthDataNoOutl = healthData[~((healthData < (Q1 - 1.5 * IQR)) |(healthData > (Q3 + 1.5 * IQR))).any(axis=1)]
healthDataNoOutl.info()


# In[33]:


plt.figure(figsize=(10,5))
c= healthDataNoOutl.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c


# All true outliers have been removed from the data frame.  
# What is left of the original group of people who became 'under 46' and 'over 104'?

# In[34]:


# Are there still lifespan-outliers here ?(Age limits chosen on sight.)
lifespOutlNoOutl = healthDataNoOutl.query("lifespan <= 46" and "lifespan >= 104") 
#display(LifespOutl)
amountLifespOutlNoOutl = lifespOutlNoOutl.count()
display(amountLifespOutlNoOutl)
# Apparently in this population there are still 30 (out of 64 people) '46 or younger' or ' 104 or older' when they died.
print()
negLifespOutlNoOutl = healthDataNoOutl.query("lifespan <= 46") 
amountNegLifespOutlNoOutl = negLifespOutlNoOutl.count()
display(amountNegLifespOutlNoOutl)
# Apparently in this new population there are still 3 (out of 9) people '46 or younger' when they died.


# ## BMI column calculated on original dataframe (with outliers)
# 
# ### What is a healthy BMI?
# BMI gives an estimate of how healthy your body weight is. You can calculate BMI for women, men and children from 2 years of age.  
# 
# BMI is less suitable if you are very muscular, pregnant, breastfeeding or of Asian descent.  
# *Note:* we have no information about the different races in our population.  
# For adults, a healthy BMI is between 18.5 and 25. But this does not apply to everyone.  
# For the elderly and children, different limits for underweight, overweight and healthy weight apply. 
# 
# ### Outcome BMI from 70 years of age
# 
# There are no official cut-off points for BMI for people aged 70 and over. In the BMI meter, we have assumed BMI limits for underweight, healthy weight and (severe) overweight to be higher than 19-69. This is due to the risk of disease.  
# This is because elderly people are only at higher risk of disease at a BMI score of 28 or higher, and are already at higher risk of malnutrition at a BMI score lower than 22.
# 
# More info on: https://www.voedingscentrum.nl/bmi

# In[35]:


#BMI-column in orig df (with outliers), rounded to 0 marks behind the '.' 

healthData['bmi'] = round(healthData['mass']/((healthData['length']**2)*0.0001))
display(healthData.head())


# In[36]:


# Boxplot 'bmi'
sns.boxplot(x=healthData['bmi'])
# There may be outliers here


# In[37]:


# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hlines.html
# matplotlib.pyplot.hlines(y, xmin, xmax, colors=None, linestyles='solid', label='', *, data=None, **kwargs)
x = healthData['lifespan']
y = healthData['bmi']
color1 = ['red']
color2 = ['yellow']
minBmi = plt.hlines(18.5, xmin = 2, xmax = 70, colors = color1)
maxBmi = plt.hlines(25, xmin = 2, xmax = 70, colors = color1)
minBmiEld = plt.hlines(22, xmin = 71, xmax = 113, colors = color1)
maxBmiEld= plt.hlines(28, xmin = 71, xmax = 113, colors = color1)
age70 = plt.vlines(70, ymin = 0, ymax = 47, colors = color2)
xlabel = plt.xlabel('Lifespan. Yellow line at age 70.')
ylabel = plt.ylabel('Bmi')
display(plt.scatter(x, y))


# I placed a yellow line at 70.  
# It strikes me (by eye) that in the group 70 years and above, the BMI of a sizable proportion of people is either too high or too low.  
# Over 70 years of age, too low Bmi seems to be common.

# In[38]:


plt.figure(figsize=(10,5))
c= healthData.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c


# In[ ]:




