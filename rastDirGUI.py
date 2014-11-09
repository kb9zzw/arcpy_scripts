#Name: rastDirGUI.py
#Purpose:  Gets a directory from a user with a GUI and prints the names of GRID raster files in the directory.
#Usage:  rastDirGUI.py
#Input:  Directory (using GUI)
#Output:  prints list of GRID rasters in directory
#Author:  Jon Burroughs (jdburou)
#Date:  3/6/2012

import arcpy
from tkFileDialog import askdirectory
from Tkinter import Tk

# some settings
initialDir = "C:/Temp"
rasterType = "GRID"
windowTitle = "Select a folder to list GRID rasters"

# set workspace from user input
parent = Tk()
arcpy.env.workspace = askdirectory(initialdir=initialDir, title=windowTitle, parent=parent)
parent.destroy()

# get list of rasters
gridRasters = arcpy.ListRasters("*", rasterType)

# print results
for file in gridRasters :
    print file