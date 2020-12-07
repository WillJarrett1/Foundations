#!/usr/bin/env python
# coding: utf-8

# # School Board Minutes
# 
# Scrape all of the school board minutes from http://www.mineral.k12.nv.us/pages/School_Board_Minutes
# 
# Save a CSV called `minutes.csv` with the date and the URL to the file. The date should be formatted as YYYY-MM-DD.
# 
# **Bonus:** Download the PDF files
# 
# **Bonus 2:** Use [PDF OCR X](https://solutions.weblite.ca/pdfocrx/index.php) on one of the PDF files and see if it can be converted into text successfully.
# 
# * **Hint:** If you're just looking for links, there are a lot of other links on that page! Can you look at the link to know whether it links or minutes or not? You'll want to use an "if" statement.
# * **Hint:** You could also filter out bad links later on using pandas instead of when scraping
# * **Hint:** If you get a weird error that you can't really figure out, you can always tell Python to just ignore it using `try` and `except`, like below. Python will try to do the stuff inside of 'try', but if it hits an error it will skip right out.
# * **Hint:** Remember the codes at http://strftime.org
# * **Hint:** If you have a date that you've parsed, you can use `.dt.strftime` to turn it into a specially-formatted string. You use the same codes (like %B etc) that you use for converting strings into dates.
# 
# ```python
# try:
#   blah blah your code
#   your code
#   your code
# except:
#   pass
# ```
# 
# * **Hint:** You can use `.apply` to download each pdf, or you can use one of a thousand other ways. It'd be good `.apply` practice though!

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

url = "http://www.mineral.k12.nv.us/pages/School_Board_Minutes"
html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")
soup


# In[ ]:


all_rows = []
rows = soup.find_all('a')

for row in rows[:74]:
    try:
        if re.search('^([/]files[/])', row.get('href')).group(1) == '/files/':
            text_date = row.text.strip()
            url = row.get('href')
            row_dict = {
                'text_date': text_date,
                'url': url
            }
            all_rows.append(row_dict)
    except:
        pass
all_rows


# In[ ]:


df = pd.DataFrame(all_rows)
df


# In[ ]:


df['month'] = df['text_date'].str.replace(r"\s\d\d?,\s\d{4}$", "")
df['day'] = df['text_date'].str.replace(r"\D", "").str[:-4].str.zfill(2)
df['year'] = df['text_date'].str.replace(r"\D", "").str[-4:]


# In[ ]:


df['date'] = pd.to_datetime(df['month'] + df['day'] + df['year'], format='%B%d%Y')
del df['month'], df['day'], df['year'], df['text_date']
df


# In[ ]:


#Save to CSV
df.to_csv('minutes.csv', index=False)


# In[ ]:


#Load from CSV
df = pd.read_csv('minutes.csv')
df


# In[ ]:


#Download files
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs',  {
    "plugins.always_open_pdf_externally": True
})

def download_url(url):
    url = "http://www.mineral.k12.nv.us" + url
    driver = webdriver.Chrome(options=options)
    driver.get(url)

df['url'].apply(download_url)

