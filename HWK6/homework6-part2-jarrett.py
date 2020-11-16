#!/usr/bin/env python
# coding: utf-8

# # Homework 6, Part Two: A dataset about dogs.
# 
# Data from [a FOIL request to New York City](https://www.muckrock.com/foi/new-york-city-17/pet-licensing-data-for-new-york-city-23826/)

# ## Do your importing and your setup

# In[ ]:


import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 200)
pd.set_option("display.max_rows", 200)


# ## Read in the file `NYC_Dog_Licenses_Current_as_of_4-28-2016.xlsx` and look at the first five rows

# In[ ]:


df = pd.read_excel("NYC_Dog_Licenses_Current_as_of_4-28-2016.xlsx", nrows=30000)
df.head(5)


# ## How many rows do you have in the data? What are the column types?
# 
# If there are more than 30,000 rows in your dataset, go back and only read in the first 30,000.

# In[ ]:


df.index
# See above


# In[ ]:


df.columns


# ## Describe the dataset in words. What is each row? List two column titles along with what each of those columns means.
# 
# For example: “Each row is an animal in the zoo. `is_reptile` is whether the animal is a reptile or not”

# #### WDJ: Each row describes a single dog for the purpose of issuing the owners a licence. Column 'Owner Zip Code' is where the owner lives. Column 'Animal Name' is the dog's name.

# # Your thoughts
# 
# Think of four questions you could ask this dataset. **Don't ask them**, just write them down in the cell below. Feel free to use either Markdown or Python comments.

# In[ ]:


# What is the most popular breed of dog?
# How have trends in dog names changed over the past x years?
# Which breeds are most commonly not vaccinated?
# Are there any areas where dogs are less likely to be vaccinated than others?


# # Looking at some dogs

# ## What are the most popular (primary) breeds of dogs? Graph the top 10.

# In[ ]:


df['Primary Breed'].value_counts().head(10).sort_values().plot.barh()


# ## "Unknown" is a terrible breed! Graph the top 10 breeds that are NOT Unknown

# In[ ]:


df[df['Primary Breed'] != 'Unknown']['Primary Breed'].value_counts().head(10).sort_values().plot.barh()


# ## What are the most popular dog names?

# In[ ]:


df[df['Animal Name'] != 'UNKNOWN']['Animal Name'].value_counts().head(10).sort_values().plot.barh()


# ## Do any dogs have your name? How many dogs are named "Max," and how many are named "Maxwell"?

# In[ ]:


df[df['Animal Name'] == 'Will']


# In[ ]:


df[df['Animal Name'] == 'Max']['Animal Name'].value_counts()


# In[ ]:


df[df['Animal Name'] == 'Maxwell']['Animal Name'].value_counts()


# ## What percentage of dogs are guard dogs?
# 
# Check out the documentation for [value counts](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html).

# In[ ]:


round(df['Guard or Trained'].value_counts(normalize=True) * 100, 2)


# ## What are the actual numbers?

# In[ ]:


df['Guard or Trained'].value_counts()


# ## Wait... if you add that up, is it the same as your number of rows? Where are the other dogs???? How can we find them??????
# 
# Use your `.head()` to think about it, then you'll do some magic with `.value_counts()`

# In[ ]:


df['Guard or Trained'].value_counts(dropna=False)


# ## Fill in all of those empty "Guard or Trained" columns with "No"
# 
# Then check your result with another `.value_counts()`

# In[ ]:


df['Guard or Trained'] = df['Guard or Trained'].fillna('No')


# In[ ]:


round(df['Guard or Trained'].value_counts(normalize=True) * 100, 2)


# ## What are the top dog breeds for guard dogs? 

# In[ ]:


guard_dogs = df[df['Guard or Trained'] == 'Yes']
guard_dogs[guard_dogs['Primary Breed'] != 'Unknown']['Primary Breed'].value_counts()


# ## Create a new column called "year" that is the dog's year of birth
# 
# The `Animal Birth` column is a datetime, so you can get the year out of it with the code `df['Animal Birth'].apply(lambda birth: birth.year)`.

# In[ ]:


df['Year'] = df['Animal Birth'].apply(lambda birth: birth.year)
df['Year']


# ## Calculate a new column called “age” that shows approximately how old the dog is. How old are dogs on average?

# In[ ]:


df['Age'] = 2020 - df['Year']


# In[ ]:


round(df['Age'].mean(), 1)


# # Joining data together

# ## Which neighborhood does each dog live in?
# 
# You also have a (terrible) list of NYC neighborhoods in `zipcodes-neighborhoods.csv`. Join these two datasets together, so we know what neighborhood each dog lives in. **Be sure to not read it in as `df`, or else you'll overwrite your dogs dataframe.**

# In[ ]:


df2 = pd.read_csv("zipcodes-neighborhoods.csv")
df2.head(5)


# In[ ]:


df.index


# ## What is the most popular dog name in all parts of the Bronx? How about Brooklyn? The Upper East Side?

# In[ ]:


full_df = df.merge(df2, left_on='Owner Zip Code', right_on='zip', how='left')


# In[ ]:


# Bronx
full_df.loc[((full_df['Animal Name'] != 'Unknown') & (full_df['borough'] == 'Bronx')), 'Animal Name'].value_counts().head(10)


# In[ ]:


# Brooklyn
full_df.loc[
    (
        (full_df['Animal Name'].str.contains('unknown', case=False) == False) &
        (full_df['borough'] == 'Brooklyn')
    ), 'Animal Name'].value_counts().head(10)


# In[ ]:


# Upper East Side
full_df.loc[
    (
        (full_df['Animal Name'].str.contains('unknown', case=False) == False) &
        (full_df['Animal Name'].str.contains('no name', case=False) == False) &
        (full_df['neighborhood'] == 'Upper East Side')
    ), 'Animal Name'].value_counts().head(10)


# ## What is the most common dog breed in each of the neighborhoods of NYC?

# In[ ]:


full_df[
    full_df['Primary Breed'].str.contains('unknown', case=False) == False]\
    .groupby('borough')['Primary Breed']\
    .value_counts()\
    .groupby(level=0)\
    .nlargest(1)\
# I'm not sure how to stop the borough column coming up twice...


# ## What breed of dogs are the least likely to be spayed? Male or female?

# In[ ]:


df_spayed = round(df.groupby('Primary Breed')['Spayed or Neut'].value_counts(normalize=True).mul(100), 1).sort_values(ascending=False).reset_index(name='Spayed or Neut perc')
df_spayed[df_spayed['Spayed or Neut'] == 'No']


# In[ ]:


df_spayed = round(df.groupby('Animal Gender')['Spayed or Neut'].value_counts(normalize=True).mul(100), 1).sort_values(ascending=False).reset_index(name='Spayed or Neut perc')
df_spayed[df_spayed['Spayed or Neut'] == 'No']


# ## Make a new column called monochrome that is True for any animal that only has black, white or grey as one of its colors. How many animals are monochrome?

# In[ ]:


df(['Animal Dominant Color'] & ['Animal Secondary Color'] & ['Animal Third Color']).str.contains('white|black|grey', case=False)
# I tried a bunch of stuff but could not figure this one out.


# ## How many dogs are in each borough? Plot it in a graph.

# In[ ]:


full_df.groupby('borough')['Animal Name'].count().sort_values().plot(kind="barh")


# ## Which borough has the highest number of dogs per-capita?
# 
# You’ll need to merge in `population_boro.csv`

# In[ ]:


df3 = pd.read_csv("boro_population.csv")
df3.head(5)


# In[ ]:


pop_df = full_df.merge(df2, left_on='Owner Zip Code', right_on='zip', how='left')
pop_df.dropna
pop_df.zip_y.astype(int)
# I can't get this change from float to int to work.


# ## Make a bar graph of the top 5 breeds in each borough.
# 
# How do you groupby and then only take the top X number? You **really** should ask me, because it's kind of crazy.

# In[ ]:


full_df[
    full_df['Primary Breed'].str.contains('unknown', case=False) == False]\
    .groupby('borough')['Primary Breed']\
    .value_counts()\
    .groupby(level=0)\
    .nlargest(5)\
    .plot(kind='barh', figsize=(10,10))
#Would be nice for this to be a stacked bar chart, but I couldn't get that working.


# ## What percentage of dogs are not guard dogs?

# In[ ]:


guard_dogs = round(df['Guard or Trained'].value_counts(normalize=True) * 100, 2).reset_index()
guard_dogs[guard_dogs['index'] == 'No']

