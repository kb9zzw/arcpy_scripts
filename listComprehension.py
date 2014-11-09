#Name: listComprehension.py
#Author:  Jon Burroughs (jdburrou)
#Date: 2/10/2012

# Create a list of all uppercase field names 
fieldNames = ['FID', 'Shape', 'COVER', 'RECNO']
fieldNames2 = [ i.upper() for i in fieldNames ]
print "1. All cap field names:", fieldNames2

# Create a list of rounded float values 
strList = ['3.34', '1.07', '4.21', '4.56', '4.5']
intList = [ round(float(i)) for i in strList ] #modified - JB
print "2. Rounded float values:", intList 

# Create a list of inverse values 
values = [8.0, 4.0, 4.0, 1.0, 5.0, 4.0, 4.0, 2.0]
inverse = [ 1/i for i in values ] #modified - JB
print "3. The inverse values:", inverse 

# Create a list from the given list as described here: Suppose each raster in the list below has a VALUE field. If you wanted to perform a weighted sum on these rasters, you'd need to create a list of rasters with weights and then join those strings into a single semicolon delimited string.This example just does one step of that process. DON'T CALCULATE a weighted sum! Here we assume that the weight we want to give the raster is encoded by the last character of the raster name and we want to use the VALUE field for calculating the sum. So we want a list were 'stw01 VALUE 1' replaces 'stw01' and 'stw02 VALUE 2' replaces 'stw02', and so forth. Watch out for spacing. ['stw01VALUE1', 'sttw03VALUE3', 'stw04VALUE4'] will NOT work! 
rasterList = [ "stw01", "sttw03", "stw04"]
rasterList2 = [ '%s VALUE %s' % (i, i[-1]) for i in rasterList ] #modified - JB
print "4. Weighted sum input:", rasterList2 

# Create a list of output file names 
inputFiles = ["COVER.shp", "Fires.shp", "Data.txt"]
outputFiles = [ i[:-4] + "out" + i[-4:] for i in inputFiles ] #modified - JB
print "5. Output files:", outputFiles

# Create a list field lengths (notice this is a field property, NOT the length of the name.). 
import arcpy
gp = arcpy
fc = "C:/Temp/COVER63p.shp"
fs = arcpy.ListFields( fc )
fieldLengths = [ i.length for i in fs ] #modified - JB
print "6. The lengths of the fields:", fieldLengths