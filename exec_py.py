import os
import sys
import subprocess

print("From python file in git")
print('Hello world', file=sys.stderr)
proc = subprocess.run(["python", "/user/home/main.py"], capture_output=True, shell=True)
print("Script:", proc.stdout)
print("Script error:", proc.stderr)
print("Python script from docker executed")

proc = subprocess.run(["dbt", "run"], capture_output=True, shell=True)
print("DBT output:", proc.stdout)
print("DBT error:", proc.stderr)
print("DBT run called")
