#user define modules

import mymodule

print(mymodule.greet("nandana"))
print(mymodule.greet1("shradha"))
print(mymodule.greet3("aira"))

from mymodule import greet1
print(greet1("shradha"))

import mymodule as m
print(m.greet("nandana"))
print(m.greet1("shradha"))
print(m.greet3("aira"))


#built-in modules
import math 
print(math.factorial(5))
print(math.sqrt(25))
print(math.pi)

import datetime
now=datetime.datetime.now()
print(now)

import os
current_dir=(os.getcwd())
print(current_dir)

import sys 
print(sys.version)

import random
a=random.randint(1,10)
print(a)

#third party library
import numpy as np
a=np.array([1,2,3,4])
print(a)
