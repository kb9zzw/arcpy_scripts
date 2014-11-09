#Name: erase.py
#Purpose: Erases fire damaged areas from park region
#Author:  Jon Burroughs (jdburrou)
#Date: 1/21/2012

import arcpy

# Set environment
arcpy.env.workspace = "C:/Temp"
arcpy.env.overwriteOutput = 1

# Set parameters
inputFeatures = "COVER63p.shp"
eraseFeatures = "special_regions.shp"
outputFeatureClass = "no_damage.shp"

# Erase features
try :
    arcpy.Erase_analysis(inputFeatures, eraseFeatures, outputFeatureClass)
except :
    arcpy.GetMessages()
    