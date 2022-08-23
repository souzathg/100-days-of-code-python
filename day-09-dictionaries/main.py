# Dictionaries in python

programming_dictionary = {
                            "Bug": "An error.",
                            "Function": "A piece of code.",
                        }

print(programming_dictionary["Bug"])

# Adding new items to dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

# Redifining a value.
programming_dictionary["Bug"] = "A moth in your computer."

#Loop through a dictionary
for key in programming_dictionary:
    # Prints the key
    print(key)
    # Prints the value
    print(programming_dictionary[key])
