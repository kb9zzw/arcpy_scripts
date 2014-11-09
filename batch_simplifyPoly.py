#Name: batch_simplifyPoly.py
#Purpose: Performs polygon simplification on all polygon shapefiles in workspace
#Input:  workspace (optional, default = "C:/Temp")
#Example:  batch_simplifyPoly.py "C:/Temp"
#Author: Jon Burroughs (jdburrou)
#Date: 2/6/2012

import arcpy, sys

# if user provides a workspace argument, use it.
# otherwise, default to C:/Temp
if len(sys.argv) > 1 :
    arcpy.env.workspace = sys.argv[1]
else :
    arcpy.env.workspace = "C:/Temp"

# overwrite output
arcpy.env.overwriteOutput = 1

# get list of shapefile features
features = arcpy.ListFeatureClasses("*.shp")

# simplify options
algorithm = "POINT_REMOVE"
tolerance = 50

# loop through features
for feature in features:
    try :
        # get the feature description
        dsc = arcpy.Describe(feature)

        # if feature is polygon, simplify it        
        if dsc.shapeType == 'Polygon' :
            output = feature[:-4] + "_simplified.shp"
            arcpy.SimplifyPolygon_cartography(feature, output, algorithm, tolerance)
    except :
        print arcpy.GetMessages()
