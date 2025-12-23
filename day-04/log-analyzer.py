#You will create a Python script that:
# You will create a Python script that:
# - Reads a log file (example: application or system log)
# - Identifies and counts:
#   - INFO
#   - WARNING
#   - ERROR messages
# - Prints a summary to the **terminal**
# - Writes the summary to an **output file**
import os   
def log_analyzer(log_file_path, output_file_path):
    info_count = 0
    warning_count = 0
    error_count = 0

    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                if "INFO" in line:
                    info_count += 1
                elif "WARNING" in line:
                    warning_count += 1
                elif "ERROR" in line:
                    error_count += 1

        summary = (
            f"Log Analysis Summary for '{os.path.basename(log_file_path)}':\n"
            f"INFO messages: {info_count}\n"
            f"WARNING messages: {warning_count}\n"
            f"ERROR messages: {error_count}\n"
        )

        # Print summary to terminal
        print(summary)

        # Write summary to output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(summary)

    except FileNotFoundError:
        print(f"The log file '{log_file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
log_file_path = 'app.log'  # Replace with your log file path
output_file_path = 'log_summary.txt'  # Replace with your desired output file path
log_analyzer(log_file_path, output_file_path)

