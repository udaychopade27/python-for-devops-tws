import os

#read file content nd then print the nalysis doen on it
def file_analysis(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            lines = content.splitlines()
            num_lines = len(lines)
            num_words = len(content.split())
            num_chars = len(content)

            print(f"File Analysis of '{os.path.basename(file_path)}':")
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_chars}")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
# Example usage
file_path = 'app.log'  # Replace with your file path
file_analysis(file_path)