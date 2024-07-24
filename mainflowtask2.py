#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[7]:


data=pd.read_csv("C:\Data Cleaning and Preprocessing.csv")


# In[8]:


type(data)


# In[29]:


data.info


# In[9]:


data.describe()


# In[10]:


#removing duplicates
data=data.drop_duplicates()
data


# In[11]:


data.isnull()


# In[12]:


data.notnull()


# In[13]:


data.isnull().sum()


# In[14]:


data.isnull().sum().sum()


# In[33]:


data2=data.fillna(value=0)
data2


# In[34]:


data3=data.fillna(method='pad')
data3


# In[35]:


data4=data.fillna(method='bfill')
data4


# In[36]:


import numpy as np
from scipy import stats


# In[37]:


#detect the outliers using IQR
data2.columns


# In[38]:


data2.drop(['Observation'],axis=1,inplace=True)
data2.columns


# In[39]:


#outliers
Q1=data2.quantile(0.25)
Q3=data2.quantile(0.75)
IQR=Q3-Q1
IQR


# In[40]:


data2=data2[~((data2<Q1-1.5*IQR)| (data2>Q3+1.5*IQR)).any(axis=1)]
print(data2)


# In[41]:


data2.describe()






