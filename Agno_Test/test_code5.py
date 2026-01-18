import subprocess
import os

# Get current directory (Python-native)
current_dir = os.getcwd()

# Create a file using a shell command
subprocess.run(["touch", "new_file.txt"], cwd=current_dir, check=True)
subprocess.run(["rm", "new_file.txt"], cwd=current_dir, check=True)


print(f"File created in: {current_dir}")

