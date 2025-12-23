# function to find cpu usage and tke cpu threshold as input 
# and if cpu usage is more than threshold print warning message and send mail
import psutil

def check_cpu_usage():
    user_cpu_threshold = float(input("Enter CPU usage threshold percentage (e.g., 75 for 75%): "))
    current_cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU Usage: {current_cpu_usage}%")
    if current_cpu_usage > user_cpu_threshold:
        print(f"Warning: CPU usage is above the threshold of {user_cpu_threshold}%!")
        # Here you can add code to send an email notification if needed
    else:
        print("CPU usage is within the acceptable range.")  
# Call the function to check CPU usage
check_cpu_usage()
# psutil library is used to get system information like cpu, memory, disk usage etc.    
# psutil.cpu_percent(interval=1) returns the current cpu usage percentage over 1 second interval    
# input() function is used to take user input from console    
# float() function is used to convert string input to float for comparison  
# if-else statement is used to check if current cpu usage is more than user defined threshold and print appropriate message
    