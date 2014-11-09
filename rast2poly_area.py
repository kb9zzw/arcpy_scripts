#Name: rast2poly_area.py
#Purpose: Calculates the area of shapes in getty_rast
#Author:  Jon Burroughs (jdburrou)
#Date: 1/21/2012

import arcpy

# Set environment
arcpy.env.workspace = "C:/Temp"
arcpy.env.overwriteOutput = 1

# Set parameters
inRaster = "getty_rast"
outFeatures = "getty_rast_with_area.shp"
fieldName = "Area"
fieldType = "double"
expression = "!shape.area!"
expressionType = "PYTHON_9.3"

try :
    # Convert raster to polygon
    arcpy.RasterToPolygon_conversion(inRaster, outFeatures)

    # Add an area field
    arcpy.AddField_management(outFeatures, fieldName, fieldType)

    # Calculate area field
    arcpy.CalculateField_management(outFeatures, fieldName, expression, expressionType)
except :
    print arcpy.GetMessages()