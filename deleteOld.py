#Name:  deleteOld.py
#Purpose:  Deletes fire entries where CalendarYe < 2000
#Usage:  deleteOld.py <inputFile>
#Example:  deleteOld.py C:/Temp/NEROfires.shp
#Author:  Jon Burroughs (jdburrou)
#Date:  2/21/2012

import sys, arcpy

# get input from user
inputFile = sys.argv[1]

try :
    cur = arcpy.UpdateCursor(inputFile)

    # delete rows older than 2000
    for row in cur :
        if row.CalendarYe < 2000 :
            cur.deleteRow(row)
except :
    # print errors
    print arcpy.GetMessages()

finally :
    # cleanup
    if row :
        del row
    if cur :
        del cur
