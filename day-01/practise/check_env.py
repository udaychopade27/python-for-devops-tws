# Get environment from user and print it
env = input("Enter your environment : ")
print("You are in the", env, "environment.")

a = input("Enter first number: ")  #  when we take user input it is considered as string
# a = int(input("Enter first number: "))
print("Data type of a is:", type(a))
b = input("Enter second number: ")
# b = int(input("Enter first number: "))
print("Data type of b is:", type(b))
# Convert inputs to integers for addition
sum_ab = int(a) + int(b)
print("The sum of a and b is:", sum_ab) 
product_ab = int(a) * int(b)
print("The product of a and b is:", product_ab)

sum = a + b  # string concatenation
print("The concatenated result of a and b is:", sum)
