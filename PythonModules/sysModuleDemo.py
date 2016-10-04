# Run this using ctrl-R (or the running man icon) and be sure to supply 
# two arguments: a name and a year, separated by spaces  - before hitting OK

import sys

name = sys.argv[1]
startDate = int(sys.argv[2])

currentYear = 2016
employmentYears = currentYear - startDate
if startDate > currentYear:
	print "Need to enter a year before 2015. Exiting"
	sys.exit(1)

print "Hello " + name
print "Seems you've been working for " + str(employmentYears) + " years"