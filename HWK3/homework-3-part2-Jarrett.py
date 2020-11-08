# Will Jarrett
# 02/11/2020
# Homework 3.2

import requests

# Documentation URL
print("------")
print("Documentation for Weather API can be found at https://www.weatherapi.com/docs/")
print("------")

# Current weather of place I was born
api_key = "?key=cfd5474aa09d4f069b7232714200211&q="
query = "folkestone"

url = ("http://api.weatherapi.com/v1/current.json" + api_key + query)
response = requests.get(url, allow_redirects=True)
data = response.json()

name = data['location']['name']
temp_c = data['current']['temp_c']

print(f"{name}: {temp_c}°C")
print("------")

# Country
print(f"{name} is in {data['location']['country']}")
print("------")

# Temperature feeling
feelslike_c = data['current']['feelslike_c']

if temp_c - feelslike_c > 0:
    print(f"In {name}, it is {temp_c}°C but it feels {temp_c - feelslike_c:.1f}°C colder.")
elif temp_c - feelslike_c < 0:
    print(f"In {name}, it is {temp_c}°C but it feels {feelslike_c - temp_c:.1f}°C warmer.")
else:
    print(f"In {name}, it is {temp_c}°C and that is exactly how it feels.")
print("------")

# Temperature at Heathrow
query = "LHR"
url = ("http://api.weatherapi.com/v1/current.json" + api_key + query)
response = requests.get(url, allow_redirects=True)
data = response.json()

name = data['location']['name']
temp_c = data['current']['temp_c']

print(f"{name}: {temp_c}°C")
print("------")

# Forecast
url = ("http://api.weatherapi.com/v1/forecast.json" + api_key + query + "&days=3")
print(f"To get a three day forecast at {name}, I would go to {url}")
print("------")

# Three dates in the forecast
response = requests.get(url, allow_redirects=True)
data = response.json()

dates = data['forecast']['forecastday']

dates_list = []
max_temp_list = []

print("The three dates in the current three-day forecast are:")
for date in dates:
    print(date['date'])
    dates_list.append(date['date'])
print("------")

# Display maximum temperature
print("The maximum temperature for each of the three days is:")
for date in dates:
    print(f"{date['day']['maxtemp_c']}°C")
    max_temp_list.append(date['day']['maxtemp_c'])
print("------")

# Display day with highest temperature
date_temp_zip = zip(max_temp_list, dates_list)
date_temp_zip = sorted(date_temp_zip, reverse=True)

print(f"Over the next three days in {data['location']['name']}, the hottest day is going to be {date_temp_zip[0][1]}, when it will be {date_temp_zip[0][0]}°C.")
print("------")
