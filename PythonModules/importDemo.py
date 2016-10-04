#importDemo.py
#
#Description:
# A simple examination of importing modules and how to access them once imported

#Use the dir() function to list all loaded modules and variables
print dir()

# Import just one component from a model
from os import path
dir() # See what was imported
print path.join("C:\\temp","myFile.txt")

# Import a module [here the numpy module], giving it a name you choose [here 'np']
import numpy as np
print dir(np)

# Import all subcomponents of a module, giving access to them 
# without needing to preface a function with the module's name
from math import *
print dir()
print sqrt(25)

# Remove reference to a specific module from your script/session
del np
print dir(np) # <-- this will now give you an error