#Name: loop_getcount.py
#Purpose: Get record count for shapefiles in workspace
#Author: Jon Burroughs (jdburrou)
#Date: 1/28/2012

import arcpy, os, re

# set workspace
arcpy.env.workspace = "C:/Temp"

# regular expression for shapfiles with
# "Fire" or "fire" in their name
pattern = re.compile("^.*(F|f)ire.*\.shp$")

# get file list
fileList = os.listdir(arcpy.env.workspace)

# loop over file list
for file in fileList :
    # if matching shapefile, then get count
    if re.search(pattern, file) :
        result = arcpy.GetCount_management(file)
        print "%s has %s entries." % (file, result)