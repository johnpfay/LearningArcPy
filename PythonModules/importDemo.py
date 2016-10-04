#Use the dir() function to list all loaded modules and variables
print dir()

# Import just one component from a model
from os import path
dir() # See what was imported
print path.join("C:\\temp","myFile.txt")

# Import a module, giving it a name you choose
import win32com.client as win32c
print dir(win32c)

# Import all subcomponents of a module, giving access to them 
# without needing to preface a function with the module's name
from math import *
print dir()
print sqrt(25)

# Remove reference to a specific module from your script/session
del win32c
print dir(win32c) # <-- this will now give you an error