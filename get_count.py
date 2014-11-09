#Name: get_count.py
#Purpose: Counts polygons in park region
#Author:  Jon Burroughs (jdburrou)
#Date: 1/21/2012

import arcpy

# Set environment
arcpy.env.workspace = "C:/Temp"
arcpy.env.overwriteOutput = 1

# Set parameters
inputFeatures = "COVER63p.shp"

# Count polygons
try :
    result = arcpy.GetCount_management(inputFeatures)
    print "There are %s polygons in %s" % (result, inputFeatures)
except :
    print arcpy.GetMessages()