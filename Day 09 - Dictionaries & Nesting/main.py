# Styling a dictionary
programming_dictionary = { 
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.", 
}

# Retrieval item of dictionary
print(programming_dictionary["Bug"])

# Adding new items in dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Edit an intem of a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Empty dictionary
# empty_dictionary = {}
# empty_dictionary = dict()

# Wipe and existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list into a dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Stuttgart", "Hamburg"],
        "visits": 3,
    },
}

# Nesting a dictionary into a list

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Stuttgart", "Hamburg"],
        "visits": 3,
    },
]