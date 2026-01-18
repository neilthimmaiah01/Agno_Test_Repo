import subprocess

command = "echo hellow"
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
