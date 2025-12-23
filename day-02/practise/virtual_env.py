#Virtaul Environmant
# A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages.
# Virtual environments are used to create isolated Python environments for different projects, allowing you to manage dependencies and avoid conflicts between packages.
# To create a virtual environment, you can use the venv module that comes with Python 3.3 and later.
# Here are the steps to create and activate a virtual environment:  
# 1. Open your terminal or command prompt.
# 2. Navigate to the directory where you want to create the virtual environment.
# 3. Run the following command to create a virtual environment named "myenv":
#    python3 -m venv myenv
# 4. Activate the virtual environment:
#    - On Windows, run: myenv\Scripts\activate
#    - On macOS and Linux, run: source myenv/bin/activate
# 5. Once activated, you can install packages using pip, and they will be installed only in the virtual environment.
# 6. To deactivate the virtual environment and return to the global Python environment, simply run the command:
#    deactivate 
# Note: Make sure you have Python installed on your system before creating a virtual environment.       
# Virtual environments are especially useful when working on multiple projects with different dependencies or when testing new packages without affecting the global Python installation.
# To delete the virtual environment, simply deactivate it (if it's active) and then delete the "myenv" directory.
# Example of creating and activating a virtual environment
# Step 1: Create a virtual environment named "myenv"
# python3 -m venv myenv
# Step 2: Activate the virtual environment
# On Windows:
# myenv\Scripts\activate
# On macOS and Linux:
# source myenv/bin/activate 
# Step 3: Install a package (e.g., requests) in the virtual environment
# pip install requests
# Step 4: Deactivate the virtual environment when done
# deactivate    
# Note: The above commands are to be run in the terminal or command prompt, not in a Python script. 
# This file is just for reference and does not contain executable code.
