#sysModuleDemo.py
#
#Description:
# This script demonstrates the use of the sys module's "argument vector", or argv, object.
# The argv is a list of values, i.e. a vector. The first value in this list (sys.argv[0] is 
# always the full path and name of the script itself. Values after that, (e.g. sys.argv[1])
# are items supplied when running the script. This is how parameters can be passed into your
# script at run-time. This, of course, is very useful as we will see...
#
#What to do: 
# Run this using ctrl-R (or the running man icon) and be sure to supply 
# two arguments: a name and a year, separated by spaces  - before hitting OK

#import the sys module
import sys

#get the two inputs supplied when the script was called
name = sys.argv[1]
startDate = int(sys.argv[2])

#run a bit of code using these values...
currentYear = 2016
employmentYears = currentYear - startDate
if startDate > currentYear:
	print "Need to enter a year before 2015. Exiting"
	sys.exit(1)

print "Hello %s! " %name,
print "Seems you've been working here for %d years" %employmentYears