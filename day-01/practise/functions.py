#functions.py
# function definition
def greet(name):
    return "Hello, " + name + "! Welcome to Python programming."        
# function call
user_name = input("Enter your name: ")
message = greet(user_name)
print(message)     

     
# function to add two numbers
def sum(a, b):
    return a + b  

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = sum(num1, num2)
print("The sum of", num1, "and", num2, "is:", result)          
# function to check if a number is even or odd