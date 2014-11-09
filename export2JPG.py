#Name:  export2JPG.py
#Purpose:  exports an mxd file to jpg
#Usage:  export2JPG.py <mxd_file>
#Example:  export2JPG.py "C:/Temp/test.mxd"
#Author:  Jon Burroughs (jdburrou)
#Date:  3/25/2012

import arcpy, sys

# get map file from user
inputMap = sys.argv[1]

# convert map to JPG
outputMap = inputMap[:-4] + ".jpg"
mxd = arcpy.mapping.MapDocument(inputMap)
arcpy.mapping.ExportToJPEG(mxd, outputMap)

# cleanup
del mxd