#!/usr/bin/env python
# coding: utf-8

# Will Jarrett
# 
# 06/11/2020
# 
# Homework 4, part 1
# 
# 
# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[ ]:


import requests


# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[ ]:


api_key = "?key=cfd5474aa09d4f069b7232714200211&q="
query = "folkestone"

url = ("http://api.weatherapi.com/v1/current.json" + api_key + query)
response = requests.get(url, allow_redirects=True)
data = response.json()

name = data['location']['name']
temp_c = data['current']['temp_c']

print(f"{name}: {temp_c}°C")


# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[ ]:


windspeed = data['current']['wind_mph']
feelslike_c = data['current']['feelslike_c']

print(f"The current windspeed in {name} is {windspeed}mph")


# In[ ]:


if temp_c - feelslike_c > 0:
    print(f"In {name}, it is {temp_c}°C but it feels {temp_c - feelslike_c:.1f}°C colder")
elif temp_c - feelslike_c < 0:
    print(f"In {name}, it is {temp_c}°C but it feels {feelslike_c - temp_c:.1f}°C warmer")
else:
    print(f"In {name}, it is {temp_c}°C and that is exactly how it feels")


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible on next Thursday?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*
# 
# WDJ: I couldn't do this for next Thursday due to limitations of the free API, so I wrote code that always finds tomorrow's info.

# In[ ]:


url = ("http://api.weatherapi.com/v1/forecast.json" + api_key + query + "&days=3")
response = requests.get(url, allow_redirects=True)
data = response.json()
name = data['location']['name']

astro = data['forecast']['forecastday'][1]['astro']['moon_illumination']
date = data['forecast']['forecastday'][1]['date']

print(f"In {name} on {date}, the moon will be {astro}% illuminated")


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[ ]:


maxtemp_c = data['forecast']['forecastday'][0]['day']['maxtemp_c']
mintemp_c = data['forecast']['forecastday'][0]['day']['mintemp_c']

print(f"In {name} today, the difference between the high and low temperatures is {maxtemp_c - mintemp_c:.1f}°C")


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# In[ ]:


url = ("http://api.weatherapi.com/v1/current.json" + api_key + query)
response = requests.get(url, allow_redirects=True)
current_data = response.json()

url = ("http://api.weatherapi.com/v1/forecast.json" + api_key + query + "&days=3")
response = requests.get(url, allow_redirects=True)
forecast_data = response.json()


# ## 5) Go through the daily forecasts, printing out the next week's worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[ ]:


day_forecasts = forecast_data['forecast']['forecastday']
name = forecast_data['location']['name']

for day_forecast in day_forecasts:
    maxtemp_c = day_forecast['day']['maxtemp_c']
    date = day_forecast['date']
    if maxtemp_c >= 25:
        print(f"In {name} on {date}, the maximum temperature is {maxtemp_c}°C. Lovely and hot!")
    elif maxtemp_c >= 5:
        print(f"In {name} on {date}, the maximum temperature is {maxtemp_c}°C. Warm enough.")
    else:
        print(f"In {name} on {date}, the maximum temperature is {maxtemp_c}°C. Bit cold!")


# # 6) What will be the hottest day in the next week? What is the high temperature on that day?

# In[ ]:


dates = forecast_data['forecast']['forecastday']
dates_list = []
max_temp_list = []

for date in dates:
    dates_list.append(date['date'])
    max_temp_list.append(date['day']['maxtemp_c'])
    
date_temp_zip = zip(max_temp_list, dates_list)
date_temp_zip = sorted(date_temp_zip, reverse=True)

print(f"Over the next three days in {name}, the hottest day is going to be {date_temp_zip[0][1]}, when it will be {date_temp_zip[0][0]}°C.")


# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# WDJ: I feel like this code is pretty inefficient, but I couldn't find any other way of doing it so that it got exactly 24 hours of future data! If you have any advice on making this less clunky I would be very appreciative.

# In[ ]:


# Get the upcoming local hour
import time

current_time = time.localtime()
current_hour = time.strftime("%H", current_time)
hour = int(current_hour) + 1
if hour == 24:
    day = 1
    hour = 0
else:
    day = 0

# Grab the right URL
query = "miami"
url = ("http://api.weatherapi.com/v1/forecast.json" + api_key + "&days=3&q=" + query)
response = requests.get(url, allow_redirects=True)
forecast_data = response.json()
name = forecast_data['location']['name']

# Go through the hours for the first day
count = 0
for i in range(hour):
    if hour < 24:
        time = forecast_data['forecast']['forecastday'][day]['hour'][hour]['time']
        temp_c = forecast_data['forecast']['forecastday'][day]['hour'][hour]['temp_c']
        cloudiness = forecast_data['forecast']['forecastday'][day]['hour'][hour]['cloud']
        if cloudiness > 50:
            print(f"{name} | {time} | {temp_c}°C | Cloudy")
        else:
            print(f"{name} | {time} | {temp_c}°C | Not cloudy")
        count += 1
        hour += 1
    else:
        break

# Work out hours left
remaining_hours = 24 - count
day += 1

# Go through hours for the second day
for i in range(remaining_hours):
    time = forecast_data['forecast']['forecastday'][day]['hour'][i]['time']
    temp_c = forecast_data['forecast']['forecastday'][day]['hour'][i]['temp_c']
    if cloudiness > 50:
        print(f"{name} | {time} | {temp_c}°C | Cloudy")
    else:
        print(f"{name} | {time} | {temp_c}°C | Not cloudy")


# # 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[ ]:


# Get the upcoming local hour
import time

current_time = time.localtime()
current_hour = time.strftime("%H", current_time)
hour = int(current_hour) + 1
if hour == 24:
    day = 1
    hour = 0
else:
    day = 0

# Grab the right URL
query = "miami"
url = ("http://api.weatherapi.com/v1/forecast.json" + api_key + "&days=3&q=" + query)
response = requests.get(url, allow_redirects=True)
forecast_data = response.json()
name = forecast_data['location']['name']

# Go through the hours for the first day
hours_count = 0
temp_over_85 = 0
for i in range(hour):
    if hour < 24:
        temp_f = forecast_data['forecast']['forecastday'][day]['hour'][hour]['temp_f']
        if temp_f > 85:
            temp_over_85 += 1
        hours_count += 1
        hour += 1
    else:
        break

# Work out hours left
remaining_hours = 24 - hours_count
day += 1

# Go through hours for the second day
for i in range(remaining_hours):
    temp_f = forecast_data['forecast']['forecastday'][day]['hour'][i]['temp_f']
    if temp_f > 85:
        temp_over_85 += 1

percentage_over_85 = temp_over_85 / 24 * 100
print(f"In the next 24 hours, the temperature in {name} is above 85°F for {percentage_over_85:.0f}% of the time")


# 
# ## 9) What was the temperature in Central Park on Christmas Day, 2015? How about 2012? 2007? How far back does the API allow you to go?
# 
# - *Tip: You'll need to use latitude/longitude. You can ask Google, it knows*
# - *Tip: Remember when latitude/longitude might use negative numbers*
# 
# WDJ: I did this for one week ago in Central Park, because the free version of the API allows only 10 days of historical data.

# In[ ]:


# Grab the right URL
query = "40.7812,-73.9665"
date = "&dt=2020-10-31"
url = ("http://api.weatherapi.com/v1/history.json" + api_key + query + date)
response = requests.get(url, allow_redirects=True)
historical_data = response.json()

# WDJ: There will probably be an error here when the date becomes more than a week old
name = historical_data['location']['name']
maxtemp_c = historical_data['forecast']['forecastday'][0]['day']['maxtemp_c']
mintemp_c = historical_data['forecast']['forecastday'][0]['day']['mintemp_c']

print(f"In {name} last week, the maximum temperature was {maxtemp_c}°C and the minimum temperature was {mintemp_c}°C")


# In[ ]:




