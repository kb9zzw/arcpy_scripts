#Name: removeLines.py
#Purpose:  Removes missing or inaccurate lines from an input file.
#Usage:  removeLines.py <inFile>
#Example:  removeLines.py C:/Temp/wheat_yield_sites.txt
#Output:  editied file in same directory as input file
#Example Output:  C:/Temp/wheat_yield_sites_edited.txt
#Author:  Jon Burroughs (jdburrou)
#Date:  2/28/2012

import sys, os

# get filename from user
filename = sys.argv[1]
outname = filename[:-4] + '_edited' + filename[-4:]

# open input and output files
infile = open(filename, 'r')
outfile = open(outname, 'w')

# transfer header to output file
header = infile.readline()
outfile.write(header)

for line in infile :
    values = line.split('\t')[1:]
    try :
        floatValues = [float(x) for x in values]
        # write lines without negative values
        if not any(n < 0 for n in floatValues) :
            outfile.write(line)
    except ValueError :
        # skip lines that don't have floats, including missing values
        continue
    
# close file   
outfile.close()