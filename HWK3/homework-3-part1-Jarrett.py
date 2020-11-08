# Will Jarrett
# 02/11/2020
# Homework 3.1

import requests

# Display documentation URL
print("-------")
print("Find API documentation at: https://pokeapi.co/docs/v2")

# Find Pokemon with ID no. 55
pokemon_id = 55
url = (f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
response = requests.get(url, allow_redirects=True)
data = response.json()

pokemon_name = data['name'].capitalize()
print("-------")
print(f"The pokemon with ID {pokemon_id} is called {pokemon_name}.")

# How tall is the pokemon?
print("-------")
print(f"{pokemon_name} is {data['height'] * 10}cm tall.")

# How many pokemon versions have there been?
version_id = 1
versions = (f"https://pokeapi.co/api/v2/version/{version_id}")
for version in versions:
    versions = (f"https://pokeapi.co/api/v2/version/{version_id}")
    version_id += 1

# Take 1 away for the extra +1 at the end of the loop, and another 1 for the final failed call
print("-------")
print(f"There are {version_id - 2} versions of pokemon.")

# The name of every electric pokemon
pokemon_type = "electric"
url = (f"https://pokeapi.co/api/v2/type/{pokemon_type}")
response = requests.get(url, allow_redirects=True)
data = response.json()

print("-------")
print("Here are all the electric pokemon:")
for pokemon in data['pokemon']:
    print(pokemon['pokemon']['name'])

# Electric type pokemons in Korean
print("-------")
print(f"In Korean, electric-type pokemon are called {data['names'][1]['name']}.")

# Compare pokemon stats
print("-------")
pokemon_list = ['eevee', 'pikachu']
pokemon_speed = []

for pokemon in pokemon_list:
    url = (f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    response = requests.get(url, allow_redirects=True)
    data = response.json()
    pokemon_speed.append(data['stats'][5]['base_stat'])

if pokemon_speed[0] > pokemon_speed[1]:
    print(f"{pokemon_list[0].capitalize()} is faster than {pokemon_list[1].capitalize()}.")
elif pokemon_speed[1] > pokemon_speed[0]:
    print(f"{pokemon_list[1].capitalize()} is faster than {pokemon_list[0].capitalize()}.")
else:
    print(f"{pokemon_list[0].capitalize()} and {pokemon_list[1].capitalize()} are the same speed.")
print("-------")