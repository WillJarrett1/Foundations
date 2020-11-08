# Will Jarrett
# 29/10/2020
# Homework 2, Part 1

###
### PART 1.1 - LISTS
###

import statistics as stat
number_list = [22, 90, 0, -10, 3, 22, 48]

print(len(number_list))

print(number_list[3])

print(number_list[1] + number_list[3])

sorted_list = sorted(number_list)
print(sorted_list[-2])

print(number_list[-1])

print((sum(number_list)) / 2)

# Use statistics module to find mean and median
median = stat.median(number_list)
mean = stat.mean(number_list)

# Figure out and print relative size of median and mean
if median > mean:
    print(f"The median of this list ({median}) is greater than the mean of this list ({mean})")
elif mean > median:
    print(f"The mean of this list ({mean}) is greater than the median of this list ({median})")
else:
    print(f"The mean of this list ({mean}) is equal to the median of this list ({median})")

###
### PART 1.2 - DICTIONARIES
###

movie = {
    'title': 'One Flew Over The Cuckoo\'s Nest',
    'year': 1975,
    'director': 'Miloš Forman'
}

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

movie['budget'] = 4400000
movie['revenue'] = 163300000

if movie['budget'] > movie['revenue']:
    print("That was a bad investment")
elif movie['revenue'] > movie['budget']:
    print("That was a great investment")
else:
    print("That was an okay investment")

NYC_borough_pop = {
    'Manhattan': 1600000,
    'Brooklyn': 2600000,
    'Bronx': 1400000,
    'Queens': 2300000,
    'Staten Island': 470000
}

print(f"Population of Brooklyn: {NYC_borough_pop['Brooklyn']:,}")

NYC_total_pop = sum(NYC_borough_pop.values())
print(f"Population of NYC: {NYC_total_pop:,}")

manhattan_percent = (NYC_borough_pop['Manhattan'] / NYC_total_pop) * 100
print(f"Percentage NYC population living in Manhattan: {manhattan_percent:.1f}%")