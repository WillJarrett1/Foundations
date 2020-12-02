#!/usr/bin/env python
# coding: utf-8

# ## Logging on
# 
# Use Selenium to visit https://webapps1.chicago.gov/buildingrecords/ and accept the agreement.
# 
# > Think about when you use `.find_element_...` and when you use `.find_elementSSS_...`

# In[1]:


import pandas as pd
import re
from selenium import webdriver


# In[2]:


driver = webdriver.Chrome()


# In[3]:


driver.get("https://webapps1.chicago.gov/buildingrecords/")


# In[4]:


driver.find_element_by_xpath('/html/body/div/div[4]/form/div[1]/div[1]/input').click()


# In[5]:


driver.find_element_by_xpath('/html/body/div/div[4]/form/div[4]/div/button').click()


# ## Searching
# 
# Search for **400 E 41ST ST**.

# In[6]:


textbox = driver.find_element_by_xpath('/html/body/div/div[4]/form/div[1]/div/input')
textbox.send_keys("400 E 41ST ST")

driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/div/button').click()


# ## Saving tables with pandas
# 
# Use pandas to save a CSV of all **permits** to `Permits - 400 E 41ST ST.csv`. Note that there are **different sections of the page**, not just one long permits table.

# In[7]:


df_permits = pd.read_html(driver.page_source)[0]
df_permits.head()


# In[8]:


df_permits.to_csv('Permits - 400 E 41ST ST.csv', index=False)


# ## Saving tables the long way
# 
# Save a CSV of all DOB inspections to `Inspections - 400 E 41ST ST.csv`, but **you also need to save the URL to the inspection**. As a result, you won't be able to use pandas, you'll need to use a loop and create a list of dictionaries.
# 
# You can use Selenium (my recommendation) or you can feed the source to BeautifulSoup. You should have approximately 157 rows.
# 
# You'll probably need to find the table first, then the rows inside, then the cells inside of each row. You'll probably use lots of list indexing. I might recommend XPath for finding the table.
# 
# *Tip: If you get a "list index out of range" error, it's probably due to an issue involving `thead` vs `tbody` elements. What are they? What are they for? What's in them? There are a few ways to troubleshoot it.*

# In[9]:


inspections_list = []
inspection_table = driver.find_elements_by_tag_name("tbody")[2]
rows = inspection_table.find_elements_by_tag_name("tr")

for row in rows:
    cell = row.find_elements_by_css_selector("*")
    results = {
        'INSP': cell[1].text,
        'inspection_date': cell[2].text,
        'status': cell[4].text,
        'type_description': cell[5].text,
        'url': cell[1].get_attribute("href"),
    }
    inspections_list.append(results)
inspections_list


# In[10]:


df_inspection = pd.DataFrame(inspections_list)
df_inspection.head()


# In[11]:


df_inspection.to_csv('Inspections - 400 E 41ST ST.csv', index=False)


# ### Loopity loops
# 
# > If you used Selenium for the last question, copy the code and use it as a starting point for what we're about to do!
# 
# If you click the inspection number, it'll open up a new window that shows you details of the violations from that visit. Count the number of violations for each visit and save it in a new column called **num_violations**.
# 
# Save this file as `Inspections - 400 E 41ST ST - with counts.csv`.
# 
# Since it opens in a new window, we have to say "Hey Selenium, pay attention to that new window!" We do that with `driver.switch_to.window(driver.window_handles[-1])` (each window gets a `window_handle`, and we're just asking the driver to switch to the last one.). A rough sketch of what your code will look like is here:
# 
# ```python
# # Click the link that opens the new window
# 
# # Switch to the new window/tab
# driver.switch_to.window(driver.window_handles[-1])
# 
# # Do your scraping in here
# 
# # Close the new window/tab
# driver.close()
# 
# # Switch back to the original window/tab
# driver.switch_to.window(driver.window_handles[0])
# ```
# 
# You'll want to play around with them individually before you try it with the whole set - the ones that pass are very different pages than the ones with violations! There are a few ways to get the number of violations, some easier than others.

# In[12]:


# Click the link that opens the new window
num_violations_list = []
inspection_table = driver.find_elements_by_tag_name("tbody")[2]
rows = inspection_table.find_elements_by_tag_name("tr")

cell_count = 1
for row in rows:
    driver.find_element_by_xpath(f'/html/body/div/div[4]/div[10]/table/tbody/tr[{cell_count}]/td[1]/a').click()
    # Switch to the new window/tab
    driver.switch_to.window(driver.window_handles[-1])
    # Do your scraping in here
    num_violations = len(driver.find_elements_by_tag_name("tr")) - 2
    # Close the new window/tab
    driver.close()
    # Switch back to the original window/tab
    driver.switch_to.window(driver.window_handles[0])
    cell_count += 1
    num_violations_list.append(num_violations)
    print(num_violations)
print(num_violations_list)
backup_list = num_violations_list


# In[14]:


#Get rid of the -2 that sneaks in due to formatting differences on pages with no violations.
cleaned_list = []
for num_violation in num_violations_list:
    if num_violation == -2:
        cleaned_list.append(0)
    else:
        cleaned_list.append(num_violation)
print(cleaned_list)


# In[17]:


df_violations_no = pd.DataFrame(cleaned_list)
df_violations_no


# In[29]:


df_inspections_violations = pd.merge(df_inspection, df_violations_no, left_index=True, right_index=True)
df_inspections_violations


# In[31]:


df_inspections_violations.columns = ['INSP', 'inspection_date', 'status', 'type_description', 'url', 'number_of_violations']
df_inspections_violations.to_csv('Inspections - 400 E 41ST ST.csv', index=False)

