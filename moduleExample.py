# Module
#A file containing Python code, is called a module

# from module_name import function_name

##########################
# import math
# print("PI is", math.pi)

# import module by renaming it
#Using as to Give a Module an Alias
import math as m
print("The value of pi is", m.pi)

# import only pi from math module
from math import pi
print("The value of pi is", pi)

# import all names from the standard module math
#Importing All Functions in a Module
from math import *
print("The value of pi is", pi)

import sys
print(sys.path)

import os
os.system('cls')

#The dir() built-in function
#We can use the dir() function to find out names that are defined inside a module.

import math

dir(math)
math.__name__

print("Hello world!", flush=True)

math.factorial(3)
math.ceil(6)
#6
math.ceil(-11)
#-11

math.ceil(4.23)
#5
math.ceil(-11.453)
#-11

math.floor(5.532)
#5
math.floor(-6.432)
#-7

#Here is how the trunc() function rounds off positive or negative numbers:

math.trunc(12.32)
#12
math.trunc(-43.24)
#-43

math.pow(2, 5)
#32.0
math.pow(5, 2.4)
#47.59134846789696

math.exp(21)
#1318815734.4832146
math.exp(-1.2)
#0.30119421191220214

math.log(4)
#1.3862943611198906
math.log(3.4)
#1.2237754316221157

#The greatest common divisor (GCD)
math.fsum() 
math.sqrt()


