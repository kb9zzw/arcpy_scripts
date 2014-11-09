#Name: tableGUI.py
#Purpose:  Prints the field names from a selected file.
#Usage:  tableGUI.py
#Input:  Filename (.shp or .dbf, using GUI)
#Output:  List of fields within the file
#Author:  Jon Burroughs (jdburou)
#Date:  3/6/2012

from arcpy import ListFields
from Tkinter import Tk
from tkFileDialog import askopenfilename

# settings
acceptTypes = [("tables", "*.dbf"), ("shapefiles", "*.shp")]
initialDir = "C:/Temp"
initialFile = "COVER63p.shp"
windowTitle="Pick a file"

# prompt for file
parent = Tk()
fileName = askopenfilename(
    filetypes=acceptTypes,
    title=windowTitle,
    initialdir=initialDir,
    initialfile=initialFile,
    parent=parent)
parent.destroy()

# get and print fields
fields = ListFields(fileName)
for field in fields :
    print field.baseName

    

