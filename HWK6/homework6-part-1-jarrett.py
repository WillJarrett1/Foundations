#!/usr/bin/env python
# coding: utf-8

# # Homework 6, Part One: Lots and lots of questions about beer

# ### Do your importing and your setup

# In[ ]:


import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 200)
pd.set_option("display.max_rows", 200)


# ## Read in the file `craftcans.csv`, and look at the first first rows

# In[ ]:


df = pd.read_csv("craftcans.csv")
df.head(5)


# ## How many rows do you have in the data? What are the column types?

# In[ ]:


print(f"Number of rows: {len(df.index)}")
print(f"Number of columns: {len(df.columns)}")


# In[ ]:


df.dtypes


# In[ ]:


for column in df.columns:
    print(df[column].isna().value_counts())


# # Checking out our alcohol

# ## What are the top 10 producers of cans of beer?

# In[ ]:


df.Brewery.value_counts().head(10)


# ## What is the most common ABV? (alcohol by volume)

# In[ ]:


df.ABV.mode()


# ## Oh, weird, ABV isn't a number. Convert it to a number for me, please.
# 
# It's going to take a few steps!
# 
# ### First, let's just look at the ABV column by itself

# In[ ]:


df.ABV.describe()


# ### Hm, `%` isn't part of  a number. Let's remove it.
# 
# When you're confident you got it right, save the results back into the `ABV` column.
# 
# - *Tip: In programming the easiest way to remove something is to *replacing it with nothing*.
# - *Tip: "nothing" might seem like `NaN` sinc we talked about it a lot in class, but in this case it isn't! It's just an empty string, like ""*
# - *Tip: `.replace` is used for replacing ENTIRE cells, while `.str.replace` is useful for replacing PARTS of cells (see my New York example)*

# In[ ]:


df.ABV = df.ABV.str.replace('%', '')


# ### Now let's turn `ABV` into a numeric data type
# 
# Save the results back into the `ABV` column (again), and then check `df.dtypes` to make sure it worked.
# 
# - *Tip: We used `.astype(int)` during class, but this has a decimal in it...*

# In[ ]:


df.ABV = df.ABV.astype(float)


# ## What's the ABV of the average beer look like?
# 
# ### Show me in two different ways: one command to show the `median`/`mean`/etc, and secondly show me a chart

# In[ ]:


df.ABV.describe()


# In[ ]:


df.ABV.sort_values().hist(bins=15)


# ### We don't have ABV for all of the beers, how many are we missing them from?
# 
# - *Tip: You can use `isnull()` or `notnull()` to see where a column is missing data.*
# - *Tip: You just want to count how many `True`s and `False`s there are.*
# - *Tip: It's a weird trick involving something we usually use to count things in a column*

# In[ ]:


df.ABV.isna().value_counts()


# # Looking at location
# 
# Brooklyn used to produce 80% of the country's beer! Let's see if it's still true.

# ## What are the top 10 cities in the US for canned craft beer?

# In[ ]:


df.Location.value_counts().head(10)


# ## List all of the beer from Brooklyn, NY

# In[ ]:


df[df.Location == 'Brooklyn, NY']


# ## What brewery in Brooklyn puts out the most cans of beer?

# In[ ]:


df[df.Location == 'Brooklyn, NY'].Brewery.value_counts().sort_values(ascending=False)


# ## What are the five most popular styles of beer produced by Sixpoint?

# In[ ]:


df[df.Brewery == 'Sixpoint Craft Ales'].Style.value_counts().sort_values(ascending=False).head(5)


# ## List all of the breweries in New York state.
# 
# - *Tip: We want to match *part* of the `Location` column, but not all of it.*
# - *Tip: Watch out for `NaN` values! You might be close, but you'll need to pass an extra parameter to make it work without an error.*

# In[ ]:


df[df.Location.str.contains("NY") == True]


# ### Now *count* all of the breweries in New York state

# In[ ]:


df.Location.str.contains("NY").value_counts()


# # Measuring International Bitterness Units
# 
# ## Display all of the IPAs
# 
# Include American IPAs, Imperial IPAs, and anything else with "IPA in it."
# 
# IPA stands for [India Pale Ale](https://www.bonappetit.com/story/ipa-beer-styles), and is probably the most popular kind of beer in the US for people who are drinking [craft beer](https://www.craftbeer.com/beer/what-is-craft-beer).

# In[ ]:


df[df.Beer.str.contains("IPA") == True]


# IPAs are usually pretty hoppy and bitter. IBU stands for [International Bitterness Unit](http://www.thebrewenthusiast.com/ibus/), and while a lot of places like to brag about having the most bitter beer (it's an American thing!), IBUs don't necessary *mean anything*.
# 
# Let's look at how different beers have different IBU measurements.

# ## Try to get the average IBU measurement across all beers

# In[ ]:


#df.IBUs.mean()
df.IBUs = df.IBUs.replace("Does not apply", np.nan)
df.IBUs = df.IBUs.astype(float)


# ### Oh no, it doesn't work!
# 
# It looks like some of those values *aren't numbers*. There are two ways to fix this:
# 
# 1. Do the `.replace` and `np.nan` thing we did in class. Then convert the column to a number. This is boring.
# 2. When you're reading in your csv, there [is an option called `na_values`](http://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.read_csv.html). You can give it a list of **numbers or strings to count as `NaN`**. It's a lot easier than doing the `np.nan` thing, although you'll need to go add it up top and run all of your cells again.
# 
# - *Tip: Make sure you're giving `na_values` a LIST, not just a string*
# 
# ### Now try to get the average IBUs again

# In[ ]:


print(f"Mean: {df.IBUs.mean()}")
print(f"Median: {df.IBUs.median()}")


# ## Draw the distribution of IBU measurements, but with *twenty* bins instead of the default of 10
# 
# - *Tip: Every time I ask for a distribution, I'm looking for a histogram*
# - *Tip: Use the `?` to get all of the options for building a histogram*
# - *Tip: Make sure your `matplotlib` thing is set up right!*

# In[ ]:


df.IBUs.sort_values().hist(bins=15)


# ## Hm, Interesting distribution. List all of the beers with IBUs above the 75th percentile
# 
# - *Tip: There's a single that gives you the 25/50/75th percentile*
# - *Tip: You can just manually type the number when you list those beers*

# In[ ]:


seventy_fifth_per = df.IBUs.quantile(q=0.75)
df[df.IBUs > seventy_fifth_per].sort_values(by="IBUs")


# ## List all of the beers with IBUs below the 25th percentile

# In[ ]:


twenty_fifth_per = df.IBUs.quantile(q=0.25)
df[df.IBUs < seventy_fifth_per].sort_values(by="IBUs")


# ## List the median IBUs of each type of beer. Graph it.
# 
# Put the highest at the top, and the missing ones at the bottom.
# 
# - Tip: Look at the options for `sort_values` to figure out the `NaN` thing. The `?` probably won't help you here.

# In[ ]:


df.groupby('Style').median('IBUs').IBUs.sort_values(na_position='first')     .plot(
        title="Average IBUs by type of beer",
        figsize=(10,50),
        kind='barh'
    )


# ## Hmmmm, it looks like they are generally different styles. What are the most common 5 styles of high-IBU beer vs. low-IBU beer?
# 
# - *Tip: You'll want to think about it in three pieces - filtering to only find the specific beers beers, then finding out what the most common styles are, then getting the top 5.*
# - *Tip: You CANNOT do this in one command. It's going to be one command for the high and one for the low.*
# - *Tip: "High IBU" means higher than 75th percentile, "Low IBU" is under 25th percentile*

# In[ ]:


df[df.IBUs > df.IBUs.quantile(q=0.75)].Style.value_counts().head(5)


# In[ ]:


df[df.IBUs < df.IBUs.quantile(q=0.25)].Style.value_counts().head(5)


# ## Get the average IBU of "Witbier", "Hefeweizen" and "American Pale Wheat Ale" styles
# 
# I'm counting these as wheat beers. If you see any other wheat beer categories, feel free to include them. I want ONE measurement and ONE graph, not three separate ones. And 20 to 30 bins in the histogram, please.
# 
# - *Tip: I hope that `isin` is in your toolbox*

# In[ ]:


round(df[df.Style.isin(['Witbier', 'Hefeweizen', 'American Pale Wheat Ale'])].IBUs.mean(), 1)


# ## Draw a histogram of the IBUs of those beers

# In[ ]:


df[df.Style.isin(['Witbier', 'Hefeweizen', 'American Pale Wheat Ale'])].IBUs.hist(bins=25)


# ## Get the average IBU of any style with "IPA" in it (also draw a histogram)

# In[ ]:


round(df[df.Style.str.contains("IPA") == True].IBUs.mean(), 1)


# In[ ]:


df[df.Style.str.contains("IPA") == True].IBUs.hist(bins=20)


# ## Plot those two histograms on top of one another
# 
# To plot two plots on top of one another, you do two steps.
# 
# 1. First, you make a plot using `plot` or `hist`, and you save it into a variable called `ax`.
# 2. You draw your second graph using `plot` or `hist`, and send `ax=ax` to it as a parameter.
# 
# It would look something like this:
# 
# ```python
# ax = df.plot(....)
# df.plot(ax=ax, ....)
# ``` 
# 
# (...except totally different)

# In[ ]:


from matplotlib import pyplot

pyplot.hist(df[df.Style.str.contains('IPA') == True].IBUs, 20, label="IPAs")
pyplot.hist(df[df.Style.isin(['Witbier', 'Hefeweizen', 'American Pale Wheat Ale'])].IBUs, 20, label="Wheat beers")
pyplot.legend(loc='upper right')
pyplot.title("IBUs of types of beer")
pyplot.show()

# I couldn't get this working in the way described above, so I used matplotlib.


# ## Compare the ABV of wheat beers vs. IPAs : their IBUs were really different, but how about their alcohol percentage?
# 
# Wheat beers might include witbier, hefeweizen, American Pale Wheat Ale, and anything else you think is wheaty. IPAs probably have "IPA" in their name.

# In[ ]:


round(df[df.Style.isin(['Witbier', 'Hefeweizen', 'American Pale Wheat Ale'])].ABV.mean(), 1)


# In[ ]:


round(df[df.Style.str.contains("IPA") == True].ABV.mean(), 1)


# In[ ]:


pyplot.hist(df[df.Style.str.contains('IPA') == True].ABV, 20, label="IPAs")
pyplot.hist(df[df.Style.isin(['Witbier', 'Hefeweizen', 'American Pale Wheat Ale'])].ABV, 20, label="Wheat beers")
pyplot.legend(loc='upper right')
pyplot.title("ABV of types of beer")
pyplot.show()

# Not sure how to deal with histogram overlap. Translucency?


# ## Good work!
# 
# If you made it this far you deserve a drink.

# In[ ]:


print("Cheers!")

