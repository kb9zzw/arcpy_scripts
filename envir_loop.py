#Name:  envir_loop.py
#Purpose: Lists geoprocessing environment variables
#Usage: envir_loop.py
#Author:  Jon Burroughs (jdburrou)
#Date: 2/12/2012

import arcpy

# hardcode workspace to C:/Temp
arcpy.env.workspace = "C:/Temp"

# get environment varia
environs = arcpy.ListEnvironments()

for env in environs :
    # output env to geoprocessing window
    arcpy.AddMessage(env)

    # print env to command window
    print env

# prompt user to close window  
raw_input("Press ENTER to close.")