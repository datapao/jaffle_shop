import os
import sys

print("From python file in git")
print('Hello world', file=sys. stderr)
os.system('python /user/home/main.py')
print("Python script from docker executed")
print('Executed (on error)', file=sys. stderr)
os.system("dbt run")
print("DBT run called")
