#Name: split.py
#Purpose: Splits park region into workzones
#Author:  Jon Burroughs (jdburrou)
#Date: 1/21/2012

import arcpy

# Set environment
arcpy.env.workspace = "C:/Temp"
arcpy.env.overwriteOutput = 1

# Set parameters
inputFeature = "COVER63p.shp"
splitFeatures = "workzones.shp"
splitField = "Zone"
outWorkspace = arcpy.env.workspace

# Split features
try :
    arcpy.Split_analysis(inputFeature, splitFeatures, splitField, outWorkspace)
except :
    print arcpy.GetMessages()
