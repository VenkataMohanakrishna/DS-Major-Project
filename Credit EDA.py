#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings("ignore")


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option("display.max_columns", None)


# In[4]:


app_data = pd.read_csv("application_data.csv")
app_data.head()


# In[5]:


app_data.info()


# In[6]:


pd.set_option('display.max_rows', 200)
app_data.isnull().mean() * 100


# In[11]:


percentage = 47
threshold = int(((100 - percentage) / 100) * app_data.shape[0] + 1)
app_df = app_data.dropna(axis=1, thresh=threshold)
app_df.head()


# In[12]:


app_df.shape


# In[13]:


app_df.isnull().mean() * 100


# In[14]:


app_df.isnull().mean() * 100


# In[15]:


app_df.info()


# In[16]:


app_df.OCCUPATION_TYPE.isnull().mean()*100


# In[17]:


app_df.OCCUPATION_TYPE.value_counts(normalize=True)*100


# In[18]:


app_df.OCCUPATION_TYPE.fillna("Others", inplace=True)
app_df.OCCUPATION_TYPE.isnull().mean()*100


# In[19]:


app_df.OCCUPATION_TYPE.value_counts(normalize=True)*100


# In[20]:


app_df.EXT_SOURCE_3.isnull().mean()*100


# In[21]:


app_df.EXT_SOURCE_3.value_counts(normalize=True)*100


# In[23]:


app_df.EXT_SOURCE_3.describe()


# In[26]:


sns.boxplot(app_df.EXT_SOURCE_3)
plt.show()


# In[27]:


app_df.EXT_SOURCE_3.fillna(app_df.EXT_SOURCE_3.median(),inplace=True)
app_df.EXT_SOURCE_3.isnull().mean()*100


# In[28]:


app_df.EXT_SOURCE_3.value_counts(normalize=True)*100


# In[29]:


app_df.isnull().mean()*100


# In[30]:


app_df.AMT_REQ_CREDIT_BUREAU_HOUR.value_counts(normalize=True)*100


# In[32]:


app_df.AMT_REQ_CREDIT_BUREAU_DAY.value_counts(normalize=True)*100


# In[33]:


cols =["AMT_REQ_CREDIT_BUREAU_HOUR","AMT_REQ_CREDIT_BUREAU_DAY","AMT_REQ_CREDIT_BUREAU_WEEK",
      "AMT_REQ_CREDIT_BUREAU_MON"]
for col in cols:
    app_df[col].fillna(app_df[col].mode()[0],inplace=True)


# In[36]:


app_df.isnull().mean()*100


# In[38]:


null_cols = list(app_df.columns[app_df.isna().any()])
len(null_cols)


# In[39]:


app_df.NAME_TYPE_SUITE.value_counts(normalize=True)*100


# In[41]:


app_df.EXT_SOURCE_2.value_counts(normalize=True)*100


# In[44]:


null_cols = list(app_df.columns[app_df.isna().any()])
len(null_cols)


# In[43]:


app_df.NAME_TYPE_SUITE.fillna(app_df.NAME_TYPE_SUITE.mode()[0],inplace=True)
app_df.CNT_FAM_MEMBERS.fillna(app_df.CNT_FAM_MEMBERS.mode()[0],inplace=True)


# In[ ]:


app_df.EXT_SOURCE_2.fillna(app_df.EXT_SOURCE_2.median(),inplace=True)
app_df.AMT_GOODS_PRICE.fillna(app_df.AMT_GOODS_PRICE.median(),inplace=True)
app_df.AMT_ANNUITY.fillna(app_df.AMT_ANNUITY.median(),inplace=True)
app_df.DEF_60_CNT_SOCIAL_CIRCLE.fillna(app_df.DEF_60_CNT_SOCIAL_CIRCLE.median(), inplace=True)
app_df.DEF_30_CNT_SOCIAL_CIRCLE.fillna(app_df.DEF_30_CNT_SOCIAL_CIRCLE.median(), inplace=True)
app_df.OBS_30_CNT_SOCIAL_CIRCLE.fillna(app_df.OBS_30_CNT_SOCIAL_CIRCLE.median(), inplace=True)
app_df.OBS_60_CNT_SOCIAL_CIRCLE.fillna(app_df.OBS_60_CNT_SOCIAL_CIRCLE.median(), inplace=True)


# In[45]:


null_cols = list(app_df.columns[app_df.isna().any()])
len(null_cols)


# In[46]:


app_df.isnull().mean()*100


# In[48]:


app_df.NAME_TYPE_SUITE.value_counts(normalize=True)*100


# In[50]:


app_df.EXT_SOURCE_2.value_counts(normalize=True)*100


# In[51]:


app_df.OBS_30_CNT_SOCIAL_CIRCLE.value_counts(normalize=True)*100


# In[52]:


app_df.isnull().mean()*100

