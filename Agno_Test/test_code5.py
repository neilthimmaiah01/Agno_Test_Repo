import subprocess

# Using shell features (e.g., pipe command)
command = "ls"
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout)
