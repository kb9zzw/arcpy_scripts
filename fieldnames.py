# Name: fieldnames.py
# Purpose: Prints the list of the field names for a given input file
# Usage:  fieldnames.py <inputFile>
# Example: fieldnames.py C:/Temp/COVER63p.shp
# Author:  Jon Burroughs (jdburrou)
# Date:  2/10/2012

import arcpy, sys

# Get input file from user
inputFile = sys.argv[1]

try :
    # Get the description of the input file
    desc = arcpy.Describe(inputFile)

    # Print list of field names for input file    
    print [ field.Name for field in desc.Fields ]
except :
    print arcpy.GetMessages()
