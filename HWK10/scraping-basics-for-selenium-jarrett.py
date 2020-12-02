#!/usr/bin/env python
# coding: utf-8

# # Scraping basics for Selenium
# 
# If you feel comfortable with scraping, you're free to skip this notebook.

# ## Part 0: Imports
# 
# Import what you need to use Selenium, and start up a new Chrome to use for scraping. You might want to copy from the [Selenium snippets](http://jonathansoma.com/lede/foundations-2018/classes/selenium/selenium-snippets/) page.
# 
# **You only need to do `driver = webdriver.Chrome()` once,** every time you do it you'll open a new Chrome instance. You'll only need to run it again if you close the window (or want another Chrome, for some reason).

# In[ ]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


# In[ ]:


driver = webdriver.Chrome()


# ## Part 1: Scraping by class
# 
# Scrape the content at http://jonathansoma.com/lede/static/by-class.html, printing out the title, subhead, and byline.

# In[ ]:


driver.get("http://jonathansoma.com/lede/static/by-class.html")


# In[ ]:


print(driver.find_elements_by_class_name("title")[0].text)
print(driver.find_elements_by_class_name("subhead")[0].text)
print(driver.find_elements_by_class_name("byline")[0].text)


# ## Part 2: Scraping using tags
# 
# Scrape the content at http://jonathansoma.com/lede/static/by-tag.html, printing out the title, subhead, and byline.

# In[ ]:


driver.get("http://jonathansoma.com/lede/static/by-tag.html")


# In[ ]:


print(driver.find_elements_by_tag_name("h1")[0].text)
print(driver.find_elements_by_tag_name("h3")[0].text)
print(driver.find_elements_by_tag_name("p")[0].text)


# ## Part 3: Scraping using a single tag
# 
# Scrape the content at http://jonathansoma.com/lede/static/by-list.html, printing out the title, subhead, and byline.
# 
# > **This will be important for the next few:** if you scrape multiples, you have a list. Even though it's Seleninum, you can use things like `[0]`, `[1]`, `[-1]` etc just like you would for a normal list.

# In[ ]:


driver.get("http://jonathansoma.com/lede/static/by-list.html")


# In[ ]:


count = 0
while True:
    try:
        print(driver.find_elements_by_tag_name('p')[count].text)
        count += 1
    except:
        break


# ## Part 4: Scraping a single table row
# 
# Scrape the content at http://jonathansoma.com/lede/static/single-table-row.html, printing out the title, subhead, and byline.

# In[ ]:


driver.get("http://jonathansoma.com/lede/static/single-table-row.html")


# In[ ]:


count = 0
while True:
    try:
        print(driver.find_elements_by_tag_name('td')[count].text)
        count += 1
    except:
        break


# ## Part 5: Saving into a dictionary
# 
# Scrape the content at http://jonathansoma.com/lede/static/single-table-row.html, saving the title, subhead, and byline into a single dictionary called `book`.
# 
# > Don't use pandas for this one!

# In[ ]:


driver.get("http://jonathansoma.com/lede/static/single-table-row.html")


# In[ ]:


book = {
    'title': driver.find_elements_by_tag_name('td')[0].text,
    'subhead': driver.find_elements_by_tag_name('td')[1].text,
    'byline': driver.find_elements_by_tag_name('td')[2].text
}
book


# ## Part 6: Scraping multiple table rows
# 
# Scrape the content at http://jonathansoma.com/lede/static/multiple-table-rows.html, printing out each title, subhead, and byline.
# 
# > You won't use pandas for this one, either!

# In[ ]:


driver.get("http://jonathansoma.com/lede/static/multiple-table-rows.html")


# In[ ]:


cells = driver.find_elements_by_tag_name('td')

for cell in cells:
    print(cell.text)


# ## Part 7: Scraping an actual table
# 
# Scrape the content at http://jonathansoma.com/lede/static/the-actual-table.html, creating a list of dictionaries.
# 
# > Don't use pandas here, either!

# In[ ]:


driver.get("http://jonathansoma.com/lede/static/the-actual-table.html")


# In[ ]:


book_list = []
count = 0

rows = driver.find_elements_by_tag_name("tr")
cell = driver.find_elements_by_tag_name('td')

for row in rows:
    book = {
        'title': cell[0 + count].text,
        'subhead': cell[1 + count].text,
        'byline': cell[2 + count].text
    }
    count += len(book)
    book_list.append(book)

book_list


# ## Part 8: Scraping multiple table rows into a list of dictionaries
# 
# Scrape the content at http://jonathansoma.com/lede/static/the-actual-table.html, creating a pandas DataFrame.
# 
# > There are two ways to do this one! One uses just pandas, the other one uses the result from Part 7.

# In[ ]:


driver.get("http://jonathansoma.com/lede/static/the-actual-table.html")


# In[ ]:


df = pd.DataFrame(book_list)
df


# ## Part 9: Scraping into a file
# 
# Scrape the content at http://jonathansoma.com/lede/static/the-actual-table.html and save it as `output.csv`

# In[ ]:


driver.get("http://jonathansoma.com/lede/static/the-actual-table.html")


# In[ ]:


df.to_csv('ExampleCSV.csv')

