#Name: bufferBranch.py
#Purpose: Buffers a shapefile
#Author: Jon Burroughs (jdburrou)
#Date: 1/25/2012
#Usage: bufferBranch.py [shapefile] {bufferDistance}
#Example:  bufferBranch.py "C:\Temp\COVER63p.shp" "200 meters"

import arcpy, sys, os

# Get input file and check if valid shapefile
inFile = os.path.normpath(sys.argv[1])
if not inFile[-4:] == '.shp' :
    print "Input data format must be shapefile.  Could not buffer input file ", inFile
    sys.exit(0)

# Check if a buffer value is provided
if len(sys.argv) == 3 :
    buffer = sys.argv[2]
    print "Buffer distance: ", buffer
else :
    print "No buffer distance given.  Used default buffer distance of 1 mile."
    buffer = "1 mile"

# Name output file
outFile = inFile[:-4] + "_buffer.shp"

# Set overwrite files
arcpy.env.overwriteOutput = 1

try :
    # Call buffer tool
    print 'Buffering output: ', outFile
    arcpy.Buffer_analysis(inFile, outFile, buffer)
except :
    # oops
    print arcpy.GetMessages()
