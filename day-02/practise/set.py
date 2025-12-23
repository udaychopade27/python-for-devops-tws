#sets
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)
# Adding an element
my_set.add(6)
print("Set after adding 6:", my_set)
# Removing an element
my_set.remove(3)
print("Set after removing 3:", my_set)
# Iterating through the set
print("Iterating through the set:")
for item in my_set:
    print(item)
# Set comprehension
squared_set = {x**2 for x in range(5)}
print("Squared Set:", squared_set)
# This code demonstrates basic set operations in Python including creation, adding and removing elements, iterating, and set comprehension.
# Sets are unordered, mutable (changeable), and do not allow duplicate elements.
# Elements are defined using curly braces {} and separated by commas.
# The add() method adds an element to the set.
# The remove() method removes a specified element from the set.
# Iteration through a set can be done using a for loop to access each element one by one.
# Set comprehension provides a concise way to create sets based on existing iterables.      
# Sets are useful for storing unique items and performing mathematical set operations like union, intersection, and difference. 
# Since sets are unordered, the elements may appear in a different order each time you print the set.
# duplicates are removed automatically when adding elements to a set.     