import os
import sys
import subprocess

print("From python file in git")
print('Hello world', file=sys.stderr)
proc = subprocess.Popen(["python", "/user/home/main.py"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print("Script:", out)
print("Script error:", err)
print("Python script from docker executed")

proc = subprocess.Popen(["dbt", "run"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print("DBT output:", out)
print("DBT error:", err)
print("DBT run called")
