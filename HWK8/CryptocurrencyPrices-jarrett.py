#!/usr/bin/env python
# coding: utf-8

# # Cryptocurrency prices
# 
# * **Filename:**  `cryptocurrencies.csv`
# * **Description:** Cryptocurrency prices for a handful of coins over time.
# * **Source:** https://coinmarketcap.com/all/views/all/ but from a million years ago (I cut and pasted, honestly)
# 
# ### Make a chart of bitcoin's high, on a weekly basis
# 
# You might want to do the cherry blossoms homework first, or at least read the part about `format=` and `pd.to_datetime`.
# 
# *Yes, that's the entire assignment. It isn't an exciting dataset, but it's just dirty enough to make charting this a useful experience.*

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


df = pd.read_csv("cryptocurrencies.csv")
df.tail()


# In[ ]:


df.columns


# In[ ]:


df.index


# In[ ]:


df.date.describe


# In[ ]:


# Isolating bitcoin
df_btc = df[df['coin'] == 'BTC']
df_btc


# In[ ]:


# Checking no date nulls
df_btc_dates = df_btc[df_btc['date'].notnull()]['date'].astype(str).to_frame()
df_btc_dates


# In[ ]:


#Converting date to datetime format
df_btc['datetime'] = pd.to_datetime(df_btc_dates['date'], format='%d-%b-%y').to_frame()


# In[ ]:


df_btc.datetime.describe


# In[ ]:


#Convert high from string to float
df_btc['high'] = df_btc['high'].str.replace(',','').astype(float)


# In[ ]:


#Plot graph
df_btc.set_index('datetime').plot(figsize=(15,10), title="Bitcoin price in $")

