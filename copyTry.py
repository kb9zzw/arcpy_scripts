#Name:  copyTry.py
#Purpose:  Copies all feature classes from one directory to another.
#Usage:  copyTry.py <source_directory> <destination_directory>
#Example:  copyTry.py C:/Temp C:/Temp/output
#Author:  Jon Burroughs (jdburrou)
#Date: 2/16/2012

import arcpy, sys

# get source & destination directories from user
sourceDir, destDir = sys.argv[1:3]

# set workspace to sourceDir
arcpy.env.workspace = sourceDir

# get list of feature classes from sourceDir
features = arcpy.ListFeatureClasses()

for feature in features :
    try :
        # copy feature
        destination = "%s/%s" % (destDir, feature)
        arcpy.Copy_management(feature, destination)
        print "Copied %s to %s" % (feature, destination)
    except :
        # print error messages if trouble copying feature
        print arcpy.GetMessages()

        
 