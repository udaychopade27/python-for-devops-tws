#list
my_list = [10, 20, 30, 40, 50]  
print("Original List:", my_list)
# Accessing elements
print("First Element:", my_list[0])
print("Last Element:", my_list[-1])
# Slicing
print("Sliced List (1 to 3):", my_list[1:4])
# Adding elements
my_list.append(60)
print("List after appending 60:", my_list)
# Removing elements
my_list.remove(30)
print("List after removing 30:", my_list)
# Iterating through the list
print("Iterating through the list:")
for item in my_list:
    print(item)
# List comprehension
squared_list = [x**2 for x in my_list]
print("Squared List:", squared_list)
# This code demonstrates basic list operations in Python including creation, accessing elements, slicing, adding and removing elements, iterating, and list comprehension.
#append , coubt and ther functions are used to perform operations on list
# Lists are ordered, mutable (changeable), and allow duplicate elements.
# Indexing starts at 0, so the first element is at index 0, the second at index 1, and so on.
# Negative indexing allows access from the end of the list, with -1 being the last element
# Slicing allows you to extract a portion of the list using the syntax list[start:end], where start is inclusive and end is exclusive.
# The append() method adds an element to the end of the list.
# The remove() method removes the first occurrence of a specified value from the list.
# List comprehension provides a concise way to create lists based on existing lists or iterables.
# Iteration through a list can be done using a for loop to access each element one by one.  
# Lists can contain elements of different data types, including integers, strings, and even other lists.
            