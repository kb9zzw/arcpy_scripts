#Name:  isPoint.py
#Purpose: Checks if an input feature layer is a point type
#Input: inputFile
#Example Input:  "C:/Temp/COVER63p.shp"
#Output:  is_point is_other (passed as parameters to a model)
#Example Output:  "False" "True"
#Author:  Jon Burroughs (jdburrou)
#Date: 2/12/2012

import arcpy, sys

# fetch the input feature layer from the user.
inputFile = arcpy.GetParameterAsText(0)

# get feature layer description
desc = arcpy.Describe(inputFile)

# if feature is a point layer, set "is_point" true
if desc.shapeType == 'Point' :
    arcpy.AddMessage("Feature is a point")
    arcpy.SetParameterAsText(1, "True")
    arcpy.SetParameterAsText(2, "False")
# otherwise, set "is_other" true
else :
    arcpy.AddMessage("Feature is not a point")
    arcpy.SetParameterAsText(1, "False")
    arcpy.SetParameterAsText(2, "True")

    

