#Name: gridToPolygon_debug.py
#Purpose: Convert a raster data set to a polygon shapefile, only if it is in ESRI 'GRID' format.
#Usage: <full path input file name> <output file name> 
#Example: "C:/My Documents/Rast1" "poly1.shp"
#Date: September 14, 2008
#Modified: Jon Burroughs (jdburrou)
#Modified Date: 2/3/2012

import arcpy, sys, os

arcpy.env.overwriteOutput = 1
arcpy.env.workspace = os.path.dirname(sys.argv[1])
InRaster = os.path.basename(sys.argv[1])
dscObject = arcpy.Describe(InRaster)
OutPolygon = sys.argv[2]
if dscObject.dataType == "RasterDataset" and dscObject.Format == "GRID" :
          arcpy.RasterToPolygon_conversion(InRaster,OutPolygon)
          print "Conversion complete to:", OutPolygon
else :
          print "Warning: Conversion not performed."
          print "Input dataType:", dscObject.dataType
          if hasattr(dscObject, "Format") :
              print "Input format:", dscObject.Format