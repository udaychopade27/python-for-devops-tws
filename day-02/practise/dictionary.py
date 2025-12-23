#dictionary
my_dict = {'Name': 'Alice', 'Age': 25, 'City': 'New York'}
print("Original Dictionary:", my_dict)
# Accessing values
print("Name:", my_dict['Name'])
print("Age:", my_dict.get('Age'))
# Adding a new key-value pair
my_dict['Occupation'] = 'Engineer'
print("Dictionary after adding Occupation:", my_dict)
# Modifying an existing value
my_dict['Age'] = 26
print("Dictionary after modifying Age:", my_dict)
# Removing a key-value pair
del my_dict['City']
print("Dictionary after removing City:", my_dict)
# Iterating through the dictionary
print("Iterating through the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print("Squared Dictionary:", squared_dict)
# This code demonstrates basic dictionary operations in Python including creation, accessing values, adding and modifying key-value pairs, removing pairs, iterating, and dictionary comprehension.
# Dictionaries are unordered, mutable (changeable), and do not allow duplicate keys.
# Key-value pairs are defined using curly braces {} and separated by commas.
# Values can be accessed using their corresponding keys.
# The get() method is used to retrieve a value for a given key, returning None if the key does not exist.
# New key-value pairs can be added by assigning a value to a new key.
# Existing values can be modified by assigning a new value to an existing key.
# Key-value pairs can be removed using the del statement followed by the key.
# Iteration through a dictionary can be done using a for loop to access each key-value pair.
# Dictionary comprehension provides a concise way to create dictionaries based on existing iterables.       
        