# Name: batch_fieldnames.py
# Purpose: Lists all the rasters in a workspace whose name contain "land", along with their field names
# Usage: batch_fieldnames.py <workpsace>
# Example: batch_fieldnames.py "C:/Temp/ncrast.mdb"
# Author:  Jon Burroughs (jdburrou)
# Date:  2/10/2012

import arcpy, sys

# Set workspace from user input
arcpy.env.workspace = sys.argv[1]

try :
    # get list of rasters in workspace with name "land"
    pattern = "*land*"
    rasters = arcpy.ListRasters(pattern)

    # loop through raster list
    for raster in rasters :
        # get description
        dsc = arcpy.Describe(raster)
        # check if description has a "Fields" attribute
        if hasattr(dsc, "Fields") :
            # print raster name and fields names
            print raster
            for field in dsc.Fields :
                print "    ", field.Name
except :
    print arcpy.GetMessages()
