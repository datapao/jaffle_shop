import os
import sys
import subprocess

print("From python file in git")
print('Hello world', file=sys.stderr)
os.system("python /user/home/main.py")
print("Python script from docker executed")

proc = subprocess.run(["dbt", "--version"], capture_output=True, shell=True)
print("DBT output:", proc.stdout)
print("DBT error:", proc.stderr)
print("DBT run called")
