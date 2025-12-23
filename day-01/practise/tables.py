num = input("Enter number of number whose table to be write: ")

for i in range(1,11):
    print(f"{num} x {i} = {int(num)*i}")
    
# string formatting using f string
# f"{variable} some text {expression}"  
# example: f"{num} x {i} = {int(num)*i}"    
# output: 5 x 1 = 5 
# where num is user input and i is loop variable from range(1,11)   
# int(num) is converting string input to integer for multiplication 
# range(1,11) generates numbers from 1 to 10 inclusive  
# multiplication table from 1 to 10 for the given number    
# Example: if user inputs 5, output will be:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50   