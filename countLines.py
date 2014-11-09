#Name: countLines.py
#Purpose:  counts the number of lines for an input file
#Usage:  countLines.py <inFile>
#Example:  countLines.py C:/Temp/threeD.dat
#Author:  Jon Burroughs (jdburrou)
#Date:  2/28/2012

import sys

# get input file from user
filename = sys.argv[1]

try :
    # open file
    infile = open(filename, 'r')
except IOError :
    print "%s does not exist." % filename
    sys.exit(0)

# count lines in file
count = 0
for line in infile :
    count += 1

# close file
infile.close()

# print results
print "%s has %d lines." % (filename, count)