import os
import sys
import subprocess

print("From python file in git")
print('Hello world', file=sys.stderr)
print("files": os.listdir("/user/home"))
with open("/user/home/main.py", "r") as file:
    for line in file:
        print(line.rstrip())
os.system("python /user/home/main.py")
print("Python script from docker executed")

proc = subprocess.run(["dbt", "--version"], capture_output=True, shell=True)
print("DBT output:", proc.stdout)
print("DBT error:", proc.stderr)
print("DBT run called")

print("Env vars:")
for name, value in os.environ.items():
    print("{0}: {1}".format(name, value))
