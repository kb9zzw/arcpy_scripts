#Name:  freq_field_loop.py
#Purpose: Performs frequency analysis on string type fields for all shapefiles in a given directory.
#Usage: freq_field_loop.py <workspace>
#Example:  freq_field_loop.py "C:/Temp"
#Author:  Jon Burroughs (jdburrou)
#Date: 2/12/2012

import arcpy, sys

# get workspace from user
arcpy.env.workspace = sys.argv[1]

# set overwrite workspace
arcpy.env.overwriteOutput = 1

try :
    # get list of shapefiles
    shapefiles = arcpy.ListFeatureClasses("*.shp")
    print "(The directory contains %d shapefiles: %s)" % (len(shapefiles), ", ".join(shapefiles))

    # loop over shapefiles
    for shapefile in shapefiles :

        # get fields from shapefile        
        fields = arcpy.ListFields(shapefile)

        # loop over fields        
        for field in fields :
            # if the field is string, perform frequency analysis
            if field.type == 'String' :
                output = "%s_%sfreq.dbf" % (shapefile[:-4], field.baseName.upper())
                res = arcpy.Frequency_analysis(shapefile, output, field.baseName)
                print output
except:
    print arcpy.GetMessages()