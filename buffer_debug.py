# Name: buffer_debug.py
# Purpose: Buffer a file by 1 mile.
# Input: Full path file name of file to buffer (optional)
# Example input: C:/Temp/COVER63p.shp
# Output: buffer shapefile (Example output named C:/Temp/COVER63p_buff.shp)
# Modified By:  Jon Burroughs (jdburrou)
# Modified Date: 2/3/2012

import arcpy, sys, os

# Set default input value
inFeatureLayer = "C:/Temp/NEROfires.shp" #should be the full path file name
distance = "1 mile" #buffer distance

# Check if user passed file argument
if len(sys.argv) > 1 :
    inFeatureLayer = sys.argv[1] #if a file name is given, use it.

# Set the current workspace to Drive C and Temp directory
arcpy.env.workspace = os.path.dirname(inFeatureLayer)
print 'Workspace Set...'

# Will let file be overwritten so works on repeated runs
arcpy.env.overwriteOutput = 1
print 'Overwrite set...'

# Moved the definition of outPutFile here so that it will be
# initialized after determining whether or not the user passed the optional
# argument.
outPutFile = inFeatureLayer[:-4]+"_buff.shp" # Set the output file name

# Call buffer
print 'Calling buffer_analysis...'
rc = arcpy.Buffer_analysis(inFeatureLayer, outPutFile, distance)
print "Created output file:", rc.getOutput(0) #print the name of the file that was created