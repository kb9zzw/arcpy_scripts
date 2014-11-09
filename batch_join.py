# Name: batch_join.py
# Purpose: Prints semicolon delimited dBase tables in a workspace
# Usage:  batch_join.py <workspace>
# Example: batch_join.py "C:/Temp"
# Author:  Jon Burroughs (jdburrou)
# Date:  2/10/2012

import arcpy, sys

# set workspace
arcpy.env.workspace = sys.argv[1]

try :
    # get dBase tables from workspace
    tables = arcpy.ListTables("*.dbf")

    # print semicolon delimited tables
    print ";".join(tables)    
except :
    print arcpy.GetMessages()