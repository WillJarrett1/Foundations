#!/usr/bin/env python
# coding: utf-8

# # Rock and Mineral Clubs
# 
# Scrape all of the rock and mineral clubs listed at https://rocktumbler.com/blog/rock-and-mineral-clubs/ (but don't just cut and paste!)
# 
# Save a CSV called `rock-clubs.csv` with the name of the club, their URL, and the city they're located in.
# 
# **Bonus**: Add a column for the state. There are a few ways to do this, but knowing that `element.parent` goes 'up' one element might be helpful.
# 
# * _**Hint:** The name of the club and the city are both inside of td elements, and they aren't distinguishable by class. Instead you'll just want to ask for all of the tds and then just ask for the text from the first or second one._
# * _**Hint:** If you use BeautifulSoup, you can select elements by attributes other than class or id - instead of `doc.find_all({'class': 'cat'})` you can do things like `doc.find_all({'other_attribute': 'blah'})` (sorry for the awful example)._
# * _**Hint:** If you love `pd.read_html` you might also be interested in `pd.concat` and potentially `list()`. But you'll have to clean a little more!_

# In[ ]:


import re
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


# In[ ]:


#Set headers and grab HTML
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

url = "https://rocktumbler.com/blog/rock-and-mineral-clubs/"
html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")
soup


# In[ ]:


all_rows = []
count = 0

for row in soup.find_all('tr'):
    #Get states
    if row.find('h3') is not None:
        try:
            state = re.search('^(\w+) Rock and Mineral Clubs', row.find('h3').string).group(1)
        except:
            pass
    else:
    #Get all other info, save to dictionary
        try:
            name = row.find('a').string
            city = row.find_all('td')[1].string
            url = row.find('a').get('href')
            count += 1
            row_dictionary = {
                'name': name,
                'city': city,
                'url': url,
                'state': state
            }
            all_rows.append(row_dictionary)
        except:
            break
all_rows


# In[ ]:


#Save to dataframe
df = pd.DataFrame(all_rows)
df


# In[ ]:


#Save to CSV
df.to_csv('rock-clubs.csv', index=False)

