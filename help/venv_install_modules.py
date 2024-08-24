import subprocess
#import os

print('Removing directory..')
command =r'rmdir /s C:\Users\stefa\OneDrive\Documenti\GitHub\Steve_Projects_Whareouse_SW\myenv'
subprocess.run(command, shell=True, capture_output=False, text=True)
#os.system(r'rmdir /s C:\Users\stefa\OneDrive\Documenti\GitHub\Steve_Projects_Whareouse_SW\myenv')
print('Creating virtual environment..')
command =r'python -m venv myenv'
subprocess.run(command, shell=True, capture_output=False, text=True)
#os.system("python -m venv myenv")
print('Activating virtual environment..')
#os.system(r"myenv\Scripts\activate")
command =r"myenv\Scripts\activate"
subprocess.run(command, shell=True, capture_output=False, text=True)
print('Installing modules')
#os.system("pip install mysql-connector-python")
#os.system("pip install maskpass")
command =r"pip install mysql-connector-python"
subprocess.run(command, shell=True, capture_output=False, text=True)
command =r"pip install maskpass"
subprocess.run(command, shell=True, capture_output=False, text=True)
print('Initializing git..')
command =r'git init'
subprocess.run(command, shell=True, capture_output=False, text=True)