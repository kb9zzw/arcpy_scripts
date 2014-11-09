#Name:  removeRastLayers.py
#Purpose: Removes all raster layers from an existing map
#Usage:  removeRastLayers.py <mxd_file>
#Example:  removeRastLayers.py "C:/Temp/test.mxd"
#Author:  Jon Burroughs (jdburrou)
#Date:  3/25/2012

import arcpy, sys

# get map from user
inputMap = sys.argv[1]

# open map document and get data frames
mxd = arcpy.mapping.MapDocument(inputMap)
dfs = arcpy.mapping.ListDataFrames(mxd)

# remove raster layers from each data frame
for df in dfs :
    layers = arcpy.mapping.ListLayers(mxd, "*", df)
    for layer in layers :
        if layer.isRasterLayer :
            arcpy.mapping.RemoveLayer(df, layer)

# save a copy of the map
outputMap = inputMap[:-4] + "2.mxd"
mxd.saveACopy(outputMap)

# and we're done
del mxd
        