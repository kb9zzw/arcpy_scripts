#Name: batch_compact.py
#Purpose: Compact a file so that it uses memory more efficiently
#Input:  workspace (optional, default = "C:/Temp")
#Example: batch_compact.py "C:/Temp"
#Author: Jon Burroughs
#Date: 2/6/2012

import arcpy, sys, os

# if user provides a workspace argument, use it.
# otherwise, default to C:/Temp
if len(sys.argv) > 1 :
    arcpy.env.workspace = sys.argv[1]
else :
    arcpy.env.workspace = "C:/Temp"

# get list of personal or file geodatabases
workspaces = arcpy.ListWorkspaces("*.mdb")

# loop through list of workspaces
for workspace in workspaces :
    try:
        # print which workspace we're working on
        print "Compacting", os.path.normpath(workspace)
        
        # Check size
        size = os.path.getsize(workspace)
        print "File size before compact:", size

        # Compact the file 
        arcpy.Compact_management(workspace)

        # Check size
        size = os.path.getsize(workspace)
        print "File size AFTER compact:", size, "\n"
    except:
        # If an error occurred when running the tool,
        # print out the error message.
        print arcpy.GetMessages( ) 
