#Name: writeReadbio.py
#Purpose:  Creates a short bio file in "C:/Temp/mybio.txt"
#Author:  Jon Burroughs (jdburrou)
#Date:  2/28/2012

# the filenane
filename = "C:/Temp/mybio.txt"

# open the file in write mode
outfile = open(filename, "w")

# write some bio info to the file
outfile.write("Name: Jon Burroughs\n")
outfile.write("Major: GIS Certificate\n")
outfile.write("Hometown: Asheville, NC\n")
outfile.write("Bio: Jon was born in the backseat of Greyhound Bus, rolling down Highway 41.\n")

# close the file
outfile.close()

# open the file in read mode
infile = open(filename, "r")

# print each line of the file
for line in infile.readlines() :
    print line,

# we're done, close the file
infile.close()