#Name:  modify.py
#Purpose:  Modifies FireName entries to all caps
#Usage:  modify.py <inputFile>
#Example:  modify.py C:/Temp/NEROfires.shp
#Author:  Jon Burroughs (jdburrou)
#Date:  2/21/2012

import sys, arcpy

# get input from user
inputFile = sys.argv[1]

try :
    cur = arcpy.UpdateCursor(inputFile)

    # modify FireName entries
    for row in cur :
        row.FireName = row.FireName.upper()
        cur.updateRow(row)

except :
    # print errors
    print arcpy.GetMessages()

finally :
    # cleanup
    if row :
        del row
    if cur :
        del cur