#BUILT IN MODULE IN PYTHON=========================
#1
# import math
# print(math.sqrt(16))
# from math import sqrt --------->we can also cal a single function only from a module
# from math import * ---using * we say that import everything from math module in my program
# print(math.factorial(5))
# print(math.pi)
# print(math.floor(5.8))

#2
# import random
# print(random.randint(1,6))

#3
# import datetime
# today = datetime.datetime.now()
# today = datetime.datetime.today()
# print(today)

#4
# import calendar
# for i in range(1,13):
#     print(calendar.month(2026,i)) #------->to print calender of a month in particular year or 

#5
# import os
# print(os.getcwd()) --------->to get current working directory

#USER DEFINED MODULE IN PYTHON====================
import mod_file1 as mf
a = int(input("Enter a : "))
b = int(input("Enter b : "))
print(mf.sum(a,b))
print(mf.diff(a,b))
print(mf.product(a,b))
print(mf.division(a,b))
print(mf.floor_division(a,b))
print(mf.modulus(a,b))
print(mf.square(a))
