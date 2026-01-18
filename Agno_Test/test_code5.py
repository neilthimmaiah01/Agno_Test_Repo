import subprocess
import os

curr_directory = os.getcwd()
print(curr_directory)

command = "echo hellow"
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
