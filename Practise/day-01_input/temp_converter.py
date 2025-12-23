#Temperature converter (Celsius ↔ Fahrenheit)
# °F = (°C × 9/5) + 32,
# °C = (°F - 32) × 5/9

def temp_converter(temp):
    f_temp = ((temp *(9/5)) + 32)
    print (f"The {temp}°C is equal to {f_temp}°F")
    
def temp_converter_fahrenheit(temp1):
    c_temp = ((temp1 - 32) * (5/9))
    print (f"The {temp1}°F is equal to {c_temp}°C")
    
temp = float(input("Enter the temp which you want to convert to Fahrenheit: "))
temp_converter(temp)
temp1 = float(input("Enter the temp which you want to convert to Celcius: "))
temp_converter_fahrenheit(temp1)