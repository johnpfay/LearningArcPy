#osModuleDemo.py
#
# Description: Demonstrates some uses of the os module and the os.path submodule
#
# Created by John Fay, Fall 2015

# import the os module
import os   

# list the contents of your V: drive
print os.listdir("V:\\") 

# print the current working directory (place from where PythonWin was started)
print os.getcwd()

# create a new folder in your V: drive
os.mkdir("V:\\osplayground")

# ensure that the folder was created (check for its existence)
print os.path.exists("V:\\osplayground")

# change the working directory to your newly created folder
os.chdir("V:\\osplayground")

# Create a new file in the current working directory, write some text, and close it
fileObj = open("myFile.txt",'w')
fileObj.write("Hello there!")
fileObj.close()

# Open the file
os.system("notepad myFile.txt")

# Rename the file
os.rename("myFile.txt", "theFile.txt")

# Use the os.path sub-module to parse the file's path into components
pathString = "V:\\osplayground\\theFile.txt"    #Make a variable of the path to avoid retyping it
print os.path.basename(pathString)          #Gets the file name (without the path)
print os.path.dirname(pathString)           #Gets the path in which the file exists

pathItems = os.path.split(pathString)       # Creates a tuple of the path and file name
print pathItems[0]                            # The path
print pathItems[1]                            # The file name

# Use the os.path.join function to join a file with its path
pathString2 = os.path.join(pathItems[0],"MyOtherFile.txt")

# Remove the [renamed] file you created
os.remove("V:\\osplayground\\theFile.txt")

# Remove the folder you created (if not in use)
os.rmdir("V:\\osplayground\\")

