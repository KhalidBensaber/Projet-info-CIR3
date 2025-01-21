import os
import subprocess

try:
    # Install dependencies from requirements.txt
    subprocess.check_call(['pip', 'install','--user', '-r', 'requirements.txt'])
    print("All dependencies have been installed successfully.")
except subprocess.CalledProcessError as e:
    print("An error occurred while installing dependencies:", e)
