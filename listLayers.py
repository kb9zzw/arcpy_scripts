#Name:  listLayers.py
#Purpose:  Lists names and data sources of layers for each frame in a map document
#Usage:  listLayers.py <mxd_file>
#Example:  listLayers.py "C:/Temp/testListFrames.mxd"
#Author:  Jon Burroughs (jdburrou)
#Date:  3/25/2012

import arcpy, sys

# get map from user
inputMap = sys.argv[1]

# get frames from map
mxd = arcpy.mapping.MapDocument(inputMap)
dfs = arcpy.mapping.ListDataFrames(mxd)

# print layer name/source for each frame
for i, df in enumerate(dfs) :
    print "Frame %d: %s" % (i, df.name)
    layers = arcpy.mapping.ListLayers(mxd, "*", df)
    for j, layer in enumerate(layers) :
        print "  Layer %d: %s  %s" % (j, layer.name, layer.dataSource)

# cleanup
del mxd