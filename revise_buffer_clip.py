#Purpose: Buffer a zone and use it to clip another file
#Author: Laura Tateosian, modified by Jon Burroughs (jdburrou)
#Date: 1/25/2012
#Usage: the shapefile to buffer, the buffer distance, the shapefile to 
#             clip, the workspace
# Example: special_regions.shp "1 mile" COVER63p.shp C:/Temp/ 
import arcpy, sys, os

# get the fire damage file and basename
fireDamage = sys.argv[1]
fireDamageBase = os.path.basename(fireDamage)

# Insert buffer in name
fireBuffer = fireDamageBase.split(".")[0] + "_buffer." + fireDamageBase.split(".")[1]

# get buffer distance
bufferDist = sys.argv[2] 

# get park filename and basename
park = sys.argv[3]
parkBase = os.path.basename(park)

# Insert damageBuffer in name
clipOutput = parkBase.split(".")[0] + "_damageBuffer." + parkBase.split(".")[1]

try:
    # Let the script over write existing files.
    arcpy.env.overwriteOutput = 1
    # Set the workspace to directory of first argument
    arcpy.env.workspace = os.path.dirname(fireDamage)

    # Call tools
    arcpy.Buffer_analysis(fireDamageBase, fireBuffer, bufferDist)
    arcpy.Clip_analysis(parkBase, fireBuffer, clipOutput ) 
except:
    print arcpy.GetMessages( )