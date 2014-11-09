#Name: listUniqueValues.py
#Purpose: lists unique values for a given filename and field
#Usage: listUniqueValues.py <fileName> <field>
#Example:  listUniqueValues.py "C:/Temp/COVER63p.shp" "COVER"
#Author:  Jon Burroughs (jdburou)
#Date:  3/6/2012

import sys, arcpy

# include this directory in PYTHONPATH
sys.path.append("C:/Temp")

import listManager

# get input
fileName, field = sys.argv[1:3]

try :
    # collect values for field
    sc = arcpy.SearchCursor(fileName)
    values = []
    for row in sc :
        values.append(row.getValue(field))

    # print unique fields
    uniqueValues = listManager.uniqueList(values)
    print uniqueValues

# cleanup    
finally :
    if row :
        del row    
    if sc :
        del sc
