#simple calculator works on user input
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


# -------- User Input --------
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nChoose an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

operation = input("Enter your choice (+, -, *, /): ")

# -------- Operation Logic --------
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operation selected"

# -------- Output --------
print("\nResult:", result)
