#daily backup script  does the compressing file also 
   
# This code creates a daily backup of the specified source directory,
# storing it in a timestamped folder within the backup directory in a zip file,
# and handles errors that may occur during the process.
import os
import shutil
from datetime import datetime
def daily_backup(source_dir, backup_dir):   
    try:
        # Create a timestamped folder name
        date_str = datetime.now().strftime("%Y-%m-%d")
        backup_subdir = os.path.join(backup_dir, f"backup_{date_str}")
        os.makedirs(backup_subdir, exist_ok=True)

        # Create a zip file of the source directory
        zip_file_path = os.path.join(backup_subdir, f"backup_{date_str}.zip")
        shutil.make_archive(base_name=zip_file_path.replace('.zip', ''), format='zip', root_dir=source_dir)

        print(f"Backup of '{source_dir}' completed successfully and stored in '{zip_file_path}'.")

    except FileNotFoundError:
        print(f"The source directory '{source_dir}' does not exist.")
    except PermissionError:
        print("Permission denied. Please check your access rights.")
    except Exception as e:
        print(f"An error occurred during backup: {e}")  
# Example usage
source_directory = '/home/ubuntu/python-for-devops-tws/day-04'  # Replace with your source directory path
backup_directory = '/home/ubuntu/python-for-devops-tws/day-04'  # Replace with your backup directory path
daily_backup(source_directory, backup_directory)    
