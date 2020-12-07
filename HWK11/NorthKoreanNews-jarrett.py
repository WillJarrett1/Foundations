#!/usr/bin/env python
# coding: utf-8

# # North Korean News
# 
# Scrape the North Korean news agency http://kcna.kp
# 
# Save a CSV called `nk-news.csv`. This file should include:
# 
# * The **article headline**
# * The value of **`onclick`** (they don't have normal links)
# * The **article ID** (for example, the article ID for `fn_showArticle("AR0125885", "", "NT00", "L")` is `AR0125885`
# 
# The last part is easiest using pandas. Be sure you don't save the index!
# 
# * _**Tip:** If you're using requests+BeautifulSoup, you can always look at response.text to see if the page looks like what you think it looks like_
# * _**Tip:** Check your URL to make sure it is what you think it should be!_
# * _**Tip:** Does it look different if you scrape with BeautifulSoup compared to if you scrape it with Selenium?_
# * _**Tip:** For the last part, how do you pull out part of a string from a longer string?_
# * _**Tip:** `expand=False` is helpful if you want to assign a single new column when extracting_
# * _**Tip:** `(` and `)` mean something special in regular expressions, so you have to say "no really seriously I mean `(`" by using `\(` instead_
# * _**Tip:** if your `.*` is taking up too much stuff, you can try `.*?` instead, which instead of "take as much as possible" it means "take only as much as needed"_

# In[ ]:


import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


# In[ ]:


driver = webdriver.Chrome()


# In[ ]:


driver.get('http://kcna.kp/kcna.user.home.retrieveHomeInfoList.kcmsf')


# In[ ]:


#Translate page to English
translate = driver.find_element_by_xpath('/html/body/center/div[1]/div[1]/div/div[2]/p/a[2]')
translate.click()


# In[ ]:


#Stick elements in list of dictionaries
all_articles = []
articles = driver.find_elements_by_class_name("titlebet")

for row in articles:
    headline = row.text
    onclick = row.get_attribute('onclick')
    article_id = re.search('fn_showArticle\("(.{9}).*', onclick).group(1)
    article_dict = {
        'headline': headline,
        'onclick': onclick,
        'article_id': article_id
    }
    all_articles.append(article_dict)
        
all_articles


# In[ ]:


#Get rid of empty rows
df = pd.DataFrame(all_articles)
df = df[df.headline != ""].reset_index(drop=True)
df


# In[ ]:


df.to_csv('nk-news.csv', index=False)

