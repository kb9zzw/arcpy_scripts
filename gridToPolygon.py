#Name: gridToPolygon.py
#Purpose: Converts GRID format raster to polygon feature class
#Author: Jon Burroughs (jdburrou)
#Date: 1/25/2012
#Usage: gridToPolygon.py [grid]
#Example: gridToPolygon.py "C:/Temp/getty_rast"

import arcpy, sys

# Get the grid file name from user
grid = sys.argv[1]

# Set overwrite
arcpy.env.overwriteOutput = 1

# Get description of input
dsc = arcpy.Describe(grid)

# If input is raster and GRID, then convert to polygon and report output
if dsc.DataType == 'RasterDataset' and dsc.Format == 'GRID' :
    # convert to polygon and report output
    output = grid + '.shp'
    try :
        arcpy.RasterToPolygon_conversion(grid, output)
        print "Converted to polygon features: ", output
    except :
        print arcpy.GetMessages()
# Otherwise, warn user that conversion was not performed
else :
    print 'Warning: conversion not performed.'

    


