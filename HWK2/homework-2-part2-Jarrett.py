# Will Jarrett
# 29/10/2020
# Homework 2, Part 2

###
### PART 2.1 - LISTS
###

countries = ['United Kingdom', 'Ireland', 'France', 'United States', 'Brazil', 'Bhutan', 'New Zealand']

# Print list
for country in countries:
    print(country)

# Sort countries alphabetically
sorted_countries = sorted(countries)

print(sorted_countries[0])

print(sorted_countries[-2])

# Delete France
sorted_countries.remove('France')

# Print alphabetised list
for country in sorted_countries:
    print(country.upper())

###
### PART 2.2 - DICTIONARIES
###

tree = {
    'name': 'The Devil\'s Tree',
    'species': 'Oak',
    'age': 200,
    'location_name': 'Bernards Township, New Jersey',
    'latitude': 40.6302,
    'longitude': -74.5831
}

print(f"{tree['name']} is {tree['age']}-year-old tree that is in {tree['location_name']}")

# Display north/south location compared to NYC
NYC_latitude = 40.7128
if NYC_latitude > tree['latitude']:
    print(f"{tree['name']} in {tree['location_name']} is south of NYC")
elif tree['latitude'] > NYC_latitude:
    print(f"{tree['name']} in {tree['location_name']} is north of NYC")
else:
    print(f"{tree['name']} in {tree['location_name']} has the same latitude as NYC")

# Ask for user's age
user_age = int(input("How old are you?"))

# Display user's age compared to the tree
if user_age > tree['age']:
    print(f"You are {user_age - tree['age']} years older than {tree['name']}")
elif tree['age'] > user_age:
    print(f"{tree['name']} was {tree['age'] - user_age} years old when you were born")
else:
    print("You are the same age as the tree!")

###
### PART 2.3 - LISTS OF DICTIONARIES
###

# Dictionaries of cities

moscow = {
    'name': 'Moscow',
    'latitude': 55.7616,
    'longitude': 37.6095
}

tehran = {
    'name': 'Tehran',
    'latitude': 35.6682,
    'longitude': 51.3744
}

falkland_islands = {
    'name': 'Falkland Islands',
    'latitude': -51.7967,
    'longitude': -58.5949
}

seoul = {
    'name': 'Seoul',
    'latitude': 37.5479,
    'longitude': 126.9419
}

santiago = {
    'name': 'Santiago',
    'latitude': -33.4460,
    'longitude': -70.6671
}

# List of city dictionaries
cities = [moscow, tehran, falkland_islands, seoul, santiago]

# Display locations in relation to equator
for city in cities:
    if city['latitude'] > 0:
        print(f"{city['name']} is above the equator")
    elif city['latitude'] < 0:
        print(f"{city['name']} is below the equator")
    else:
        print(f"{city['name']} is on the equator")
    if city == falkland_islands:
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")

# Display locations in relation to tree
for city in cities:
    if city['latitude'] > tree['latitude']:
        print(f"{city['name']} is north of {tree['name']}")
    elif city['latitude'] < tree['latitude']:
        print(f"{city['name']} is south of {tree['name']}")
    else:
        print(f"{city['name']} is on the same latitude as {tree['name']}")