#count_other_debug.py
#Purpose: Count the number of records with a cover type that is NOT woods and NOT orch in an input file
# with a field named COVER.
#Input: full path shapefile name of a shapefile with a COVER field.
#Example input: "C:/Temp/COVER63p.shp"
#Output: A count of non-woods, non-orch records.
#Author: Laura Tateosian Sep 4, 2008
#Modified by:  Jon Burroughs (jdburrou), 2/21/2012, Fixed logic error in "if" statement

import arcpy, sys 

filename = sys.argv[1] # Get the full path shapefile name
sc = arcpy.SearchCursor(filename) # Get a search cursor object to loop through the file

count = 0 #Initialize the count to zero 

for line in sc :
    cover = line.COVER
    if cover != "woods" and cover != "orch" :
        count = count + 1 

print "Number of records with other cover types:", count 
del line
del sc