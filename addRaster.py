#Name:  addRaster.py
#Purpose: Adds a raster to an existing map
#Usage:  addRaster.py <mxd_file> <raster>
#Example:  addRaster.py "C:/Temp/test.mxd" "C:/Temp/getty_rast"
#Author:  Jon Burroughs (jdburrou)
#Date:  3/25/2012

import arcpy, sys

# get input from user
inputMap, raster = sys.argv[1:3]

# setup map document and dataframe
mxd = arcpy.mapping.MapDocument(inputMap)
dfs = arcpy.mapping.ListDataFrames(mxd)
df = dfs[0]

# add raster layer to map
layer = arcpy.mapping.Layer(raster)
arcpy.mapping.AddLayer(df, layer)

# save copy of map
outputMap = inputMap[:-4] + "2.mxd"
mxd.saveACopy(outputMap)

# Q.E.D.
del mxd
