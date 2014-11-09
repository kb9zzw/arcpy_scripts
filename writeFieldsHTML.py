#Name: writeFieldsHTML.py
#Purpose:  Creates HTML report of fields in a shapefile
#Usage:  writeFieldsHTML.py <shapeFile>
#Example:  writeFieldsHTML.py "C:/Temp/COVER63p.shp"
#Author:  Jon Burroughs (jdburrou)
#Date:  4/16/2012

import sys, os, arcpy

# Get shapefile from user
input = sys.argv[1]
shapeFile = os.path.basename(input)
htmlFile = input[:-4] + ".html"

# Unpack field names and wrap in HTML <li>
listItems = [ "      <li>%s</li>" % i.name \
              for i in arcpy.ListFields(input) ]

# HTML
html = """<!DOCTYPE html>
<html>
  <body>
    <h1>{0} Fields</h1>
    <ul>
{1}
    </ul>
  </body>
</html>
""".format(shapeFile, "\n".join(listItems))

# Write HTML to output file
out = open(htmlFile, "w")
out.write(html)
out.close()