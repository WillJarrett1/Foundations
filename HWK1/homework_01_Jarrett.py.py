# Will Jarrett
# 26th October 2020
# Homework 1

# Store current year
current_year = 2020

# Record year of birth and validate
while True:
    year = input("What year were you born?")
    if not year.isdigit() or int(year) > current_year:
        print(f"Please enter a year under {str(current_year)}!")
    elif int(year) == current_year:
        print("You're a bit young for this program - come back next year?")
    else:
        break

#work out approximate age
year = int(year)
age = current_year - year

# Age
print(f"You are {age} years old")

# Human heartbeats
print(f"Your heart has beaten {age * 35000000:,} times")

# Whale heartbeats
print(f"If you were a whale, your heart would have beaten {age * 10512000:,} times")

#Rabbit heartbeats
if age * 94608000 < 1000000:
    print(f"If you were a rabbit, your heart would have beaten {age * 94608000:,} times")
else:
    print(f"If you were a rabbit, your heart would have beaten {round(age * 94.608000):,} million times")

# Venus years
print(f"You are {round(age * 1.624, 1)} Venus years old")

# Neptune years
print(f"You are {round(age / 164.8, 3)} Neptune years old")

# Older/younger
if age > 25:
    print(f"You are older than me by {age - 25} years")
elif age < 25:
    print(f"You are younger than me by {25 - age} years")
else:
    print("You are the same age as me!")

# Even/odd
if year % 2 == 0:
    print("You were born in an even year")
else:
    print("You were born in an odd year")

# Democratic presidents / Which president?
if year < 1960:
    print("Born before 1960? Who knows who was president back then...")
elif year == 1960:
    print("There have been 5 Democractic presidents in your lifetime")
    print("Dwight D. Eisenhower was in power the year you were born")
elif year in range(1961, 1964):
    print("There have been 5 Democractic presidents in your lifetime")
    print("John F. Kennedy was in power the year you were born")
elif year in range(1964, 1970):
    print("There have been 4 Democractic presidents in your lifetime")
    print("Lyndon B. Johnson was in power the year you were born")
elif year in range(1970, 1975):
    print("There have been 3 Democractic presidents in your lifetime")
    print("Richard Nixon was in power the year you were born")
elif year in range(1975, 1978):
    print("There have been 3 Democractic presidents in your lifetime")
    print("Gerald Ford was in power the year you were born")
elif year in range(1978, 1982):
    print("There have been 3 Democractic presidents in your lifetime")
    print("Jimmy Carter was in power the year you were born")
elif year in range(1982, 1990):
    print("There have been 2 Democractic presidents in your lifetime")
    print("Ronald Reagan was in power the year you were born")
elif year in range(1990, 1994):
    print("There have been 2 Democractic presidents in your lifetime")
    print("George H.W. Bush was in power the year you were born")
elif year in range(1994, 2002):
    print("There have been 2 Democractic presidents in your lifetime")
    print("Bill Clinton was in power the year you were born")
elif year in range(2002, 2010):
    print("There has been 1 Democractic president in your lifetime")
    print("George W. Bush was in power the year you were born")
elif year in range(2010, 2018):
    print("There has been 1 Democractic president in your lifetime")
    print("Barack Obama was in power the year you were born")
elif year in range(2018, 2020):
    print("There have been no Democratic presidents in your lifetime")
    print("Donald Trump was in power the year you were born")