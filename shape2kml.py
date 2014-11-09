#Name: shape2kml.py
#Purpose: Converts a shapefile to kmz
#Author: Jon Burroughs (jdburrou)
#Date: 1/25/2012
#Usage: shape2kml.py [shapefile] [workspace] [kmzFile] [scale]

import arcpy, sys, os

# Get shapefile from user and check that it is a shapefile (by name)
shapefile = sys.argv[1]
if not shapefile[-3:] == 'shp' :
    raise ValueError('A shapefile is required')

# Get workspace from user
arcpy.env.workspace = sys.argv[2]

# Get KMZ filename from user and check it
kmzFile = sys.argv[3]
if not kmzFile[-3:] == 'kmz' :
    raise ValueError('A "kmz" or "kml" file is required.')

# Get scale from user
try :
    scale = int(sys.argv[4])
except ValueError :
    raise ValueError('An integer scale value is required')

# Allow overwrite of exisiting files
arcpy.env.overwriteOutput = 1

# Set output layer, based on shapefile name
outLayer = shapefile[:-3] + "lyr"

# Call tools
try :
    # Make feature layer from shapefile
    arcpy.MakeFeatureLayer_management(inFeatures, outLayer)

    # Convert layer to KMZ
    arcpy.LayerToKML_conversion(outLayer, kmzFile, scale)
except :
    # Boo boo occurred, punt
    print arcpy.GetMessages()
    

