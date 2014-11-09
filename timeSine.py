#Name: timeSine.py
#Purpose: Reports time of sine function on a given raster
#Usage: timeSine.py <inputFile> <outputFile>
#Example:  timeSine.py C:/Temp/getty_rast C:/Temp/getty_rast_sine
#Author:  Jon Burroughs (jdburou)
#Date:  3/6/2012

import sys, arcpy

sys.path.append("C:/Temp")

import timeReport

# setup arcpy
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = 1

# get input from user
inFile, outFile = sys.argv[1:3]

# time sine function
start = timeReport.getTime()
outSine = arcpy.sa.Sin(inFile)
outSine.save(outFile)
end = timeReport.getTime()

# produce a report
timeReport.diffTime(start, end, message="Calculating sine took:")