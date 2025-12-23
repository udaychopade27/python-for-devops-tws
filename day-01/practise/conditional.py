env = input("Enter your environment : ")
if env == "production":
    print("You are in the production environment.")     
elif env == "staging":
    print("You are in the staging environment.")
elif env == "development":
    print("You are in the development environment.")
else:
    print("Unknown environment.")
# conditional statements: if, elif, else          

a = int(input("Enter first number: ")   )
b = int(input("Enter second number: ")  )
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
# nested if statements

# check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number") 
     
# check if a number is positive, negative or zero
num = float(input("Enter a number: "))
if num > 0:
    print(num, "is a positive number")
elif num < 0:
    print(num, "is a negative number")
else:
    print("The number is zero")     