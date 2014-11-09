#Name: freq.py
#Purpose: Calculates frequency of coverage types within park region
#Author:  Jon Burroughs (jdburrou)
#Date: 1/21/2012

import arcpy

# Set environment
arcpy.env.workspace = "C:/Temp"
arcpy.env.overwriteOutput = 1

# Set parameters
inTable = "COVER63p.shp"
outTable = "COVER_freq.dbf"
frequencyField = "COVER"

# Calculate frequency
try :
    arcpy.Frequency_analysis(inTable, outTable, frequencyField)
except :
    print arcpy.GetMessages()