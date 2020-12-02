#!/usr/bin/env python
# coding: utf-8

# # Texas Cosmetologist Violations
# 
# Texas has a system for [searching for license violations](https://www.tdlr.texas.gov/cimsfo/fosearch.asp). You're going to search for cosmetologists!

# ## Setup: Import what you'll need to scrape the page
# 
# We'll be using Selenium for this, *not* BeautifulSoup and requests.

# In[ ]:


import pandas as pd
import re
from selenium import webdriver


# ## Starting your search
# 
# Starting from [here](https://www.tdlr.texas.gov/cimsfo/fosearch.asp), search for **cosmetologist violations** for people with the last name **Nguyen**.

# In[ ]:


driver = webdriver.Chrome()


# In[ ]:


driver.get("https://www.tdlr.texas.gov/cimsfo/fosearch.asp")


# In[ ]:


#select 'cosmetologist'
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[3]/td/select/option[10]').click()


# In[ ]:


#type in Nguyen
textbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[7]/td/p/input')
textbox.send_keys("Nguyen")


# In[ ]:


#search
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[18]/td/input[1]').click()


# ## Scraping
# 
# Once you are on the results page, do this.

# ### Loop through each result and print the entire row
# 
# Okay wait, that's a heck of a lot. Use `[:10]` to only do the first ten (`listname[:10]` gives you the first ten).

# In[ ]:


rows = driver.find_elements_by_tag_name("tr")

for row in rows[:10]:
    print(row.text)


# ### Loop through each result and print each person's name
# 
# You'll get an error because the first one doesn't have a name. How do you make that not happen?! If you want to ignore an error, you use code like this:
# 
# ```python
# try:
#    # try to do something
# except:
#    # Instead of stopping on an error, it'll jump down here instead
#    print("It didn't work')
# ```
# 
# It should help you out. If you don't want to print anything, you can type `pass` instead of the `print` statement. Most people use `pass`, but it's also nice to print out debug statements so you know when/where it's running into errors.
# 
# **Why doesn't the first one have a name?**

# In[ ]:


#I don't think this is the way we were intended to do the work but I think it returns the right results.
rows = driver.find_elements_by_tag_name("tr")

for row in rows[1:11]:
    print(row.find_elements_by_css_selector("*")[1].text)


# ## Loop through each result, printing each violation description ("Basis for order")
# 
# > - *Tip: You'll get an error even if you're ALMOST right - which row is causing the problem?*
# > - *Tip: You can get the HTML of something by doing `.get_attribute('innerHTML')` - it might help you diagnose your issue.*
# > - *Tip: Or I guess you could just skip the one with the problem...*

# In[ ]:


for row in rows[1:11]:
    print(row.find_elements_by_css_selector("*")[25].text)


# ## Loop through each result, printing the complaint number
# 
# - TIP: Think about the order of the elements

# In[ ]:


for row in rows[1:11]:
    print(row.find_elements_by_css_selector("*")[19].text)


# ## Saving the results
# 
# ### Loop through each result to create a list of dictionaries
# 
# Each dictionary must contain
# 
# - Person's name
# - Violation description
# - Violation number
# - License Numbers
# - Zip Code
# - County
# - City
# 
# Create a new dictionary for each result (except the header).
# 
# > *Tip: If you want to ask for the "next sibling," you can't use `find_next_sibling` in Selenium, you need to use `element.find_element_by_xpath("following-sibling::div")` to find the next div, or `element.find_element_by_xpath("following-sibling::*")` to find the next anything.

# In[ ]:


results_list = []

for row in rows[1:11]:
    cell = row.find_elements_by_css_selector("*")
    results = {
        'name': cell[1].text,
        'violation_description': cell[25].text,
        'violation_no': cell[19].text,
        'license_no': cell[15].text,
        'zip_code': cell[10].text,
        'county': cell[7].text,
        'city': cell[4].text
    }
    results_list.append(results)
    
print(results_list)


# ### Save that to a CSV
# 
# - Tip: Use `pd.DataFrame` to create a dataframe, and then save it to a CSV.

# In[ ]:


df = pd.DataFrame(results_list)
df


# In[ ]:


df.to_csv('TexasCosmetology.csv', index=False)


# ### Open the CSV file and examine the first few. Make sure you didn't save an extra weird unnamed column.

# In[ ]:


df_check = pd.read_csv('TexasCosmetology.csv')
df_check.head()


# ## Let's do this an easier way
# 
# Use Selenium and `pd.read_html` to get the table as a dataframe.

# In[ ]:


driver.get("https://www.tdlr.texas.gov/cimsfo/fosearch.asp")


# In[ ]:


#select 'cosmetologist'
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[3]/td/select/option[10]').click()
#type in Nguyen
textbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[7]/td/p/input')
textbox.send_keys("Nguyen")
#search
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[18]/td/input[1]').click()


# In[ ]:


df = pd.read_html(driver.page_source)[0]
df.head()

