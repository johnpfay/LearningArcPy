#arcpyModuleDemo.py
#
#Description:
# Commands to import and discover the ArcPy module

#Import the arcpy module
##This a moment as your machine needs to contact the license server
import arcpy

#List the functions that come with ArcPy
print dir(arcpy)

#Display the help on arcpy
help(arcpy)

#Display the help on just the network analyst
help(arcpy.na)

#Display the help on just the spatial analyst slope command
help(arcpy.sa.Slope)