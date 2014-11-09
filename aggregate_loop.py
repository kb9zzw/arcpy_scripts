#Name: aggregate_loop.py
#Purpose: Aggregates polygons at various distances
#Author: Jon Burroughs (jdburrou)
#Date: 1/28/2012

import arcpy

# set environment
arcpy.env.workspace = "C:/Temp"
arcpy.env.overwriteOutput = 1

# input shapefile
input = "COVER63p.shp"

# aggregation units
units = "meters"

# loop over aggregation distances
for distance in range(100,1001,100) :
    # output file
    output = input[:-4] + str(distance) + "_agg.shp"

    # distance string for AggregatePolygons
    distanceString = "%d %s" % (distance, units)    
    
    # aggregate
    arcpy.AggregatePolygons_cartography(input, output, distanceString)
    
    # report what happened
    print "%s aggregation: %s" % (distanceString, output)