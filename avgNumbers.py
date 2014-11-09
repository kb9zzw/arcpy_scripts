#Name: avgNumbers.py
#Purpose:  finds averages for each line in a file
#          with tab-delimited numeric values
#Usage:  avgNumbers.py <inFile>
#Example:  avgNumbers.py C:/Temp/crop_yield.txt
#Output:  out.txt in same directory as input file
#Author:  Jon Burroughs (jdburrou)
#Date:  2/28/2012

import sys, os

# get filename from user
in_name = sys.argv[1]
dir = os.path.dirname(filename)
out_name = '%s/out.txt' % dir

# open input/output files
infile = open(in_name, 'r')
outfile = open(out_name, 'w')

# process each line and calculate average
for line in infile :
    stringList = line.split('\t')
    floatList = [float(x) for x in stringList]
    average = sum(floatList) / len(floatList)
    outfile.write('%f\n' % average)

# close the output file
outfile.close()


