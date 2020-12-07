#!/usr/bin/env python
# coding: utf-8

# # Scraping one page per row
# 
# Let's say we're interested in our members of Congress, because who isn't? Read in `congress.csv`.

# In[ ]:


import requests
import re
import pandas as pd
import time
from bs4 import BeautifulSoup


# In[ ]:


#Load from CSV
df = pd.read_csv('congress.csv')
df


# In[ ]:


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}


# # Let's scrape one
# 
# The `slug` is the part of the URL that's particular to that member of Congress. So `/james-abdnor/A000009` really means `https://www.congress.gov/member/james-abdnor/A000009`.
# 
# Scrape his name, birthdaye, party, whether he's currently in congress, and his bill count (don't worry if the bill count is dirty, you can clean it up later).

# In[ ]:


url = "https://www.congress.gov/member/steven-palazzo/P000601"
html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")
soup


# In[ ]:


#Name
name = re.search(r"^\w+\s(.+)", soup.find(class_='legDetail').next).group(1)
name


# In[ ]:


#Senate or rep?
sen_rep = re.search(r"^(\w+)\s.+", soup.find(class_='legDetail').next).group(1)
sen_rep


# In[ ]:


#Birth year
birth_year = re.search(r"^\((\d\d\d\d)", soup.find(class_='birthdate').string.strip()).group(1)
birth_year


# In[ ]:


#Party
party = soup.find(class_='member_party').next_sibling.next_sibling.string
party


# In[ ]:


#Current member?
try:
    end_of_term = re.search(r"(.{7}$)", soup.find(class_='birthdate').next_sibling.string.strip()).group(1)
    if end_of_term == "Present":
        current_member = "Yes"
    else:
        current_member = "No"
except:
    current_member = "ERROR"
current_member


# In[ ]:


#Number of bills
bills = re.search(r"^of (.+)$", soup.find(class_="results-number").find('strong').next.next.strip()).group(1).replace(",", "")
bills


# # Build a function
# 
# Write a function called `scrape_page` that makes a URL out of the the `slug`, like we're going to use `.apply`.

# In[ ]:


whole_urls = []
def scrape_page(slug):
    whole_urls.append("https://www.congress.gov/member/" + slug)
    
df['slug'].apply(scrape_page)
whole_urls


# # Do the scraping
# 
# Rewrite `scrape_page` to actually scrape the URL. You can use your scraping code from up above. Start by testing with just one row (I put a sample call below) and then expand to your whole dataframe.
# 
# Save the results as `scraped_df`.
# 
# * **Hint:** Be sure to use `return`!
# * **Hint:** Make sure you return a `pd.Series`

# In[ ]:


all_rows = []

def scrape_page(slug):
    try:
        #Get URLs
        url = "https://www.congress.gov/member/" + slug
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, "html.parser")

        #Scrape
        name = re.search(r"^\w+\s(.+)", soup.find(class_='legDetail').next).group(1)
        sen_rep = re.search(r"^(\w+)\s.+", soup.find(class_='legDetail').next).group(1)
        birth_year = re.search(r"^\((\d\d\d\d)", soup.find(class_='birthdate').string.strip()).group(1)
        if soup.find(class_='member_party') is None:
            party = soup.find(class_='member_party_history').next_sibling.next_sibling.text.strip()
        else:
            party = soup.find(class_='member_party').next_sibling.next_sibling.string
        end_of_term = soup.find(class_='birthdate').next_sibling.text.strip()
        if "Present" in end_of_term:
            current_member = "Yes"
        else:
            current_member = "No"
        bills = re.search(r"^of (.+)$", soup.find(class_="results-number").find('strong').next.next.strip()).group(1).replace(",", "")

        #Put into dictionary
        rows_dict = {
        'name': name,
        'sen_rep': sen_rep,
        'birth_year': birth_year,
        'party': party,
        'current_member': current_member,
        'bills': bills,
        'url': url,
        }

        all_rows.append(rows_dict)
        print(url)
    except:
        rows_dict = {
        'name': 'ERROR',
        'sen_rep': 'ERROR',
        'birth_year': 'ERROR',
        'party': 'ERROR',
        'current_member': 'ERROR',
        'bills': 'ERROR',
        'url': 'ERROR',
        }
        all_rows.append(rows_dict)
        print(url)
    return

#Set off function
df['slug'].apply(scrape_page)
all_rows


# ## Join with your original dataframe
# 
# Join your new data with your original data, adding the `_scraped` suffix on the new columns. You can use either `.join` or `.merge`, but be sure to read the docs to know the difference!

# In[ ]:


#My code keeps getting stuck about halfway through. No error message, just no more progress.
#I will come back to this and have a go at chopping the csv into smaller pieces to make it more manageable,
#but for now I am going to move on.


# ## Save it
# 
# Save your combined results to `congress-plus-scraped.csv`.

# In[ ]:




