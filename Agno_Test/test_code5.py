import subprocess

# Using shell features (e.g., pipe command)
command = "ls -l | grep my_file"
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout)
