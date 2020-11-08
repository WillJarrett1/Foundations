#!/usr/bin/env python
# coding: utf-8

# # Last FM API (Music)
# 
# Spotify's API is dead to us, so we're using Last.fm's - it's still music, just not as nice of an API.
# 
# 1. Create an account at https://www.last.fm/api/
# 2. Create an "application" to get a key: https://www.last.fm/api/account/create
#     - It isn't a real application, it's just your project
#     - Name/description doesn't matter, ignore callback key and callback url
# 3. And save the API key that shows up on the next screen: 28bd18ddd528bc51b21784cef19daebe
# 
# You can find documentation at https://www.last.fm/api/
# 
# The domain for the API is `http://ws.audioscrobbler.com`, so all of your endpoints will be connected to that. To test your API key, check the following URL in your browser: `http://ws.audioscrobbler.com/2.0/?method=artist.search&artist=cher&api_key=28bd18ddd528bc51b21784cef19daebe&format=json`.
# 
# > Last.fm used to be called **AudioScrobbler**, which is why its URLs don't have "last.fm" in them.
# > While we're asking about URLs, notice that the API endpoints have a lot of `?` and `&` in them - these are key/value pairs, kind of like dictionaries, but for URLs instead of Python.

# # FIRST: SETUP

# ## 1) Import the libraries/packages you might need
# 
# We need a library to read in the data for us! We don't like `urllib2`, so it must be something cooler and better.

# In[ ]:


# Import what you need here
import requests


# ## 2) Save your API key
# 
# Write your API key here so you don't forget it - it's the "api key" one, not the "shared secret" one
# 
# 28bd18ddd528bc51b21784cef19daebe

# ## 3) The death of an API
# 
# I used to have some code here that allowed you to display images, but _the images don't work any more._ Let this be an important lesson: when you depend on external services, they can die at any time.

# # NOW: YOUR ASSIGNMENT

# ## 1) Search for and print a list of 50 musicians with `lil` in their name, along with the number of listeners they have
# 
# There are a lot of musicians with "Lil" in their name - it used to be all Lil Wayne and Lil Kim, but we live in a new world now!
# 
# - *Tip: Remember, the domain for the API is `http://ws.audioscrobbler.com`*
# - *Tip: Make sure you ask the API for 50 musicians! This involves adding another parameter to the URL - notice they all have a `&` before them. [Read the documentation](http://www.last.fm/api/show/artist.search) to find the parameter's name.* 
# - *Tip: When you are looking at any piece of data - is it a dictionary? Look at the keys! Is it a list? Look at the first element!*
# - *Tip: LOOK AT THE KEYS. and then the other keys and the other keys and the other keys. It's an ugly series of dictionaries!*

# In[ ]:


api_key = "28bd18ddd528bc51b21784cef19daebe"
artist_query = "lil"
limit = "50"

url = ("http://ws.audioscrobbler.com/2.0/?method=artist.search&artist=" + artist_query + "&api_key=" + api_key + "&limit=" + limit + "&format=json" )
response = requests.get(url, allow_redirects=True)
data = response.json()


# In[ ]:


lils = data['results']['artistmatches']['artist']

for lil in lils:
    name = lil['name']
    listeners = lil['listeners']
    print(f"{name} has {listeners} listeners")


# ## 2) How many listeners does your list have in total?
# 
# The answer should be roughly **15,000,000**. If it's lower, make sure you have 50 artists instead of 30 artists.
# 
# - *Tip: What's the data type of the `listeners` count? It's going to cause a problem!*
# - *Tip: If you were crazy you could use sum and a list comprehension. But you really don't have to!*

# In[ ]:


total_listeners = 0
for lil in lils:
    listeners = lil['listeners']
    total_listeners += int(listeners)
    
print(f"The top 50 'Lil artists have a total of {total_listeners:,} listeners between them")


# ## 3) Show each artist's name and the URL to the extra-large image
# 
# The images don't work any more, but we'll print their URLs out anyway.

# Each artist **has a list of images of different sizes**. We're interested in the second-to-last one, where `size` is `extralarge`. Print their name and use `display_image` to display their extra-large image.
# 
# - *Tip: The URL should look like this: `https://lastfm-img2.akamaized.net/i/u/300x300/0fc7d7a1812dc79e9925d80382cde594.png`*
# - *Tip: You can always assume it's the second to the last, or assume it's `extralarge`, or whatever you want to do to find it.*
# - *Tip: Make sure the URL is correct before you try to display it.*
# 
# Your output should look something like
# 
# ```
# Lil' Wayne
# https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png
# ---
# LIL UZI VERT
# https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png
# ---
# Lily Allen
# https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png
# ---
# ```
# 
# (but with more people, obviously)

# In[ ]:


for lil in lils:
    print(lil['name'])
    print(lil['image'][-2]['#text'])
    print("---")


# ## 4) Find Lil Jon's `mbid` (or anyone else's!).
# 
# Oftentimes in an API, you can do a few things: you can **search** for items, and you can **see more information** about items. To find more information about the item, you need to use their **unique id**. In this dataset, it's called an `mbid` (MusicBrainz, I think - another company associated with last.fm!).
# 
# Go through the artists and print their **name and mbid**. Find Lil Jon's `mbid`. I *wanted* Lil Uzi Vert's, but for some reason it isn't there. Then I wanted us to look at Lily Allen's, but I just couldn't bring myself to do that. If you'd rather do someone else, go for it.

# In[ ]:


search_name = "Lily Allen"

for lil in lils:
    name = lil['name']
    if name == search_name:
        mbid = lil['mbid']
        print(f"{name} | {mbid}")


# ## 5) Find the artist's name and bio using their `mbid`.
# 
# It can either be Lil Jon or whoever you selected above.
# 
# If you look at the [last.fm documentation](http://www.last.fm/api/show/artist.getInfo), you can see how to use the artist's `mbid` to find more information about them. Print **every tag associated with your artist**.
# 
# - *Tip: It's a new request to the API*
# - *Tip: Use the `mbid`, and make sure you delete the `&name=Cher` from the sample endpoint*
# - *Tip: If you use `print` for the bio it looks a little nicer than it would otherwise*

# In[ ]:


api_key = "28bd18ddd528bc51b21784cef19daebe"
mbid = "6e0c7c0e-cba5-4c2c-a652-38f71ef5785d"

url = ("http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&mbid=" + mbid + "&user=WDJ&api_key=" + api_key + "&format=json")
response = requests.get(url, allow_redirects=True)
mbid_data = response.json()

name = mbid_data['artist']['name']
bio = mbid_data['artist']['bio']['summary']

print(name)
print(bio)


# ## 6) Print every tag of that artist

# In[ ]:


name = mbid_data['artist']['name']
tags = mbid_data['artist']['tags']['tag']
all_tags = []

print(f"{name} tags:")
for tag in tags:
    all_tags.append(tag['name'])
print(', '.join(all_tags))


# # GETTING A LITTLE CRAZY
# 
# So you know your original list of musicians? I want to get tag data for ALL OF THEM. How are we going to do that?
# 
# ## 7) Find the mbids (again)
# 
# If we have a musician with an mbid of `AAA-AAA-AAA`, we get their info from a url like `http://ws.audioscrobbler.com/blahblah/?api_key=12345&mbid=AAA-AAA-AAA`.
# 
# |artist|url|
# |---|---|
# |`AAA-AAA-AAA`|`http://ws.audioscrobbler.com/blahblah/?api_key=12345&mbid=AAA-AAA-AAA`|
# |`BBB-BBB-BBB`|`http://ws.audioscrobbler.com/blahblah/?api_key=12345&mbid=BBB-BBB-BBB`|
# |`CCC-CCC-CCC`|`http://ws.audioscrobbler.com/blahblah/?api_key=12345&mbid=CCC-CCC-CCC`|
# 
# I guess we should start trying to get a list of all of the mbids.
# 
# **Loop through your artists, and print out the `mbid` for each artist**
# 
# - *Tip: You probably need to request your artist search result data again, because you probably saved over `data` with your other API request. Maybe call it `artist_data` this time?*
# - *Tip: If the artist does NOT have an `mbid`, don't print it.*

# In[ ]:


api_key = "28bd18ddd528bc51b21784cef19daebe"
artist_query = "lil"
limit = "50"

url = ("http://ws.audioscrobbler.com/2.0/?method=artist.search&artist=" + artist_query + "&api_key=" + api_key + "&limit=" + limit + "&format=json" )
response = requests.get(url, allow_redirects=True)
artist_data = response.json()


# In[ ]:


mbids = artist_data['results']['artistmatches']['artist']

for mbid in mbids:
    if mbid['mbid'] != "":
        print(mbid['mbid'])


# ## 8) Saving those mbids
# 
# For those `mbid` values, instead of printing them out, save them to a new list of just mbid values. Call this list `mbids`.
# 
# - *Tip: Use `.append` to add a single element onto a list*

# In[ ]:


mbids_list = []

for mbid in mbids:
    if mbid['mbid'] != "":
        mbids_list.append(mbid['mbid'])
print(mbids_list)


# ## 9) Printing our API urls
# 
# To get tag data for each artist, you need to use those `mbid` values to access their artist page on the API. Loop through the mbids, displying the URL you'll need to access.
# 
# - *Tip: You don't want to use a comma when printing, because commas add spaces into your text and URLs can't have that*
# - *Tip: Make sure your URL has `artist.getinfo` in it - if not, you're using the wrong endpoint.*

# In[ ]:


api_key = "28bd18ddd528bc51b21784cef19daebe"
for mbid in mbids_list:
    url = ("http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&mbid=" + mbid + "&user=WDJ&api_key=" + api_key + "&format=json")
    response = requests.get(url, allow_redirects=True)
    mbid_data = response.json()
    print(url)


# ## OKAY HERE IS A LITTLE INFORMATION: Using our API urls
# 
# This time instead of just *displaying* the URL, we're going to *request and process it*. **But first I'm going to teach you something.**
# 
# When you're dealing with an API, you don't want to make a million requests, have bad code, and then need to do those million requests again. It's usually best to test your code with a few of the results first.
# 
# So, if we have a list of numbers like this:

# In[ ]:


numbers = [4, 5, 6, 7]
numbers


# You can actually say to Python, **give me the first two**, and it will only give you the first two.

# In[ ]:


numbers[:2]


# The is **very convenient** with loopng with APIs, because instead of trying to use all FIFTY artists, you can just say "hey, please try this out with 2 of them" and you don't waste time.

# ## 10) Using the first three `mbids`, request the API urls and print the artist's name.
# 
# You built the URLs in the last question, now it's time to use them! Use `requests` etc to grab the URL and get out the artist's name.
# 
# - *Tip: The code is the same as last time you got an artist's name from their info page, it's just going to be inside of a loop*
# - *Tip: USE `PRINT` TO SEE WHAT YOU ARE LOOKING AT!!!!!*

# In[ ]:


api_key = "28bd18ddd528bc51b21784cef19daebe"
for mbid in mbids_list[:3]:
    url = ("http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&mbid=" + mbid + "&user=WDJ&api_key=" + api_key + "&format=json")
    response = requests.get(url, allow_redirects=True)
    mbid_data = response.json()
    
    name = mbid_data['artist']['name']
    bio = mbid_data['artist']['bio']['summary']
    print(name)


# ## 11) Using the first three `mbids`, request the API urls and print the artist's name and their tags
# 
# - *Tip: The code is the same as last time you got an artist's name from their info page, it's just going to be inside of a loop*
# - *Tip: It's a for loop in a for loop!*

# In[ ]:


api_key = "28bd18ddd528bc51b21784cef19daebe"
for mbid in mbids_list[:3]:
    url = ("http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&mbid=" + mbid + "&user=WDJ&api_key=" + api_key + "&format=json")
    response = requests.get(url, allow_redirects=True)
    mbid_data = response.json()
    
    name = mbid_data['artist']['name']
    bio = mbid_data['artist']['bio']['summary']    
    tags = mbid_data['artist']['tags']['tag']
    all_tags = []

    print(f"{name} tags:")
    for tag in tags:
        all_tags.append(tag['name'])
    print(', '.join(all_tags))
    print("---")


# ## 12) Using the first ten mbids, print the artist's name and whether they're a rapper
# 
# Only print their name ONCE and only print whether they are hip hop or not ONCE.
# 
# - *Tip: Rap tags include hip hop, swag, crunk, rap, dirty south, and probably a bunch of other stuff! You can include as many categories as you'd like.*
# - *Tip: You can use `2 in [1, 2, 3]` to find out if `2` is in the list of `[1, 2, 3]`.*
# - *Tip: Every time you look at a new artist, you can say they are NOT a rapper. And once you find out one of their tags is hip hop or rap, then you can note that they're a rapper. Then once you're done looking at their tags, then you can say HEY this is a rapper, or HEY this is not a rapper.*

# In[ ]:


api_key = "28bd18ddd528bc51b21784cef19daebe"
types_of_rap = ["HIP HOP", "HIP-HOP", "SWAG", "RAP", "CRUNK", "DIRTY SOUTH", "MEMPHIS RAP"]

for mbid in mbids_list[:10]:
    url = ("http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&mbid=" + mbid + "&user=WDJ&api_key=" + api_key + "&format=json")
    response = requests.get(url, allow_redirects=True)
    mbid_data = response.json()
    
    name = mbid_data['artist']['name']
    bio = mbid_data['artist']['bio']['summary']    
    tags = mbid_data['artist']['tags']['tag']
    all_tags = []
    
    do_they_rap = 0
    for tag in tags:
        if tag['name'].upper() in types_of_rap:
            do_they_rap += 1
            
    if do_they_rap > 0:
        print(f"{name}: YES to hip hop")
    else:
        print(f"{name}: NO to hip hop")


# ## 13) What percent of "lil" results are rappers?

# In[ ]:


api_key = "28bd18ddd528bc51b21784cef19daebe"
types_of_rap = ["HIP HOP", "HIP-HOP", "SWAG", "RAP", "CRUNK", "DIRTY SOUTH", "MEMPHIS RAP"]
no_of_rappers = 0

for mbid in mbids_list:
    url = ("http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&mbid=" + mbid + "&user=WDJ&api_key=" + api_key + "&format=json")
    response = requests.get(url, allow_redirects=True)
    mbid_data = response.json()
    
    name = mbid_data['artist']['name']
    bio = mbid_data['artist']['bio']['summary']    
    tags = mbid_data['artist']['tags']['tag']
    all_tags = []
    
    do_they_rap = 0
    for tag in tags:
        if tag['name'].upper() in types_of_rap:
            do_they_rap += 1
    
    if do_they_rap > 0:
        no_of_rappers += 1

percentage_of_rappers = no_of_rappers / len(mbids_list) * 100
print(f"The percentage of rappers in our selection is {percentage_of_rappers:.1f}%")


# ## 14) Seriously you are all-powerful now.

# In[ ]:


print("Hooray!")


# In[ ]:




