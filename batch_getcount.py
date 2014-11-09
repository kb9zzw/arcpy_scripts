#Name: batch_getcount.py
#Purpose: Gets feature count for each shapefile in a workspace
#Input:  workspace (optional, default = "C:/Temp")
#Example:  batch_getcount.py "C:/Temp"
#Author: Jon Burroughs (jdburrou)
#Date: 2/4/2012

import arcpy, sys

# if user provides a workspace argument, use it.
# otherwise, default to C:/Temp
if len(sys.argv) > 1 :
    arcpy.env.workspace = sys.argv[1]
else :
    arcpy.env.workspace = "C:/Temp"

# get list of shapefile features
features = arcpy.ListFeatureClasses("*.shp")

# loop through features
for feature in features:
    try :
        # get count if feature is "Point"
        dsc = arcpy.Describe(feature)    
        if dsc.shapeType == 'Point' :
            res = arcpy.GetCount_management(feature)
            print "%s has %s entries." % (feature, res.getOutput(0))
    except :
        print arcpy.GetMessages()
