#Name:  countWalk.py
#Purpose:  Recursively print entry count for all shapefiles in a given directory.
#Usage:  countWalk.py <input_dir>
#Example:  countWalk.py "C:/Temp/Data"
#Author:  Jon Burroughs (jdburrou)
#Date:  3/23/2012

import arcpy, sys, os

# get input dir from user
input_dir = sys.argv[1]

# scan input_dir recursively and print entry counts for shapefiles
for root, dirs, files in os.walk(input_dir) :
    arcpy.env.workspace = root
    for file in files :
        if file.endswith(".shp"):
            result = arcpy.GetCount_management(file)
            path = os.path.normpath("%s/%s" % (root, file))
            print "%s has %s entries" % (path, result)