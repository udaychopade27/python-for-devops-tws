#tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)
# Accessing elements
print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])        
# Slicing
print("Sliced Tuple (1 to 3):", my_tuple[1:4])      
# Iterating through the tuple
print("Iterating through the tuple:")
for item in my_tuple:
    print(item)
# Tuple comprehension (using generator expression)
squared_tuple = tuple(x**2 for x in range(5))
print("Squared Tuple:", squared_tuple)
# This code demonstrates basic tuple operations in Python including creation, accessing elements, slicing, iterating, and tuple comprehension.
# Tuples are ordered, immutable (unchangeable), and allow duplicate elements.
# Indexing starts at 0, so the first element is at index 0, the second at index 1, and so on.
# Negative indexing allows access from the end of the tuple, with -1 being the last element.
# Slicing allows you to extract a portion of the tuple using the syntax tuple[start:end], where start is inclusive and end is exclusive.
# Iteration through a tuple can be done using a for loop to access each element one by one.     
# Tuple comprehension is not directly supported, but you can use a generator expression inside the tuple() constructor to achieve similar results.
# Tuples can contain elements of different data types, including integers, strings, and even other
# tuples.   
# Since tuples are immutable, you cannot add, remove, or modify elements after the tuple is created.
# Tuples are often used to group related data together and can be used as keys in dictionaries due to their immutability.
# Example of creating and accessing a tuple
# Step 1: Create a tuple
# my_tuple = (1, 2, 3, 4, 5)
# Step 2: Access elements
# first_element = my_tuple[0]
# last_element = my_tuple[-1]
# Step 3: Slice the tuple
# sliced_tuple = my_tuple[1:4]
# Step 4: Iterate through the tuple
# for item in my_tuple:
#     print(item)
# Step 5: Create a squared tuple using generator expression
# squared_tuple = tuple(x**2 for x in range(5))
# Note: Tuples are defined using parentheses () and elements are separated by commas.