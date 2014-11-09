#Name:  point_distance.py
#Purpose:  Creates distance tables between fire stations and schools for
#          search radius values of 1-5 miles.
#Usage:  point_distance.py
#Author:  Jon Burroughs (jdburrou)
#Date: 3/24/2012

import arcpy

# environment settings
arcpy.env.workspace = "C:/Temp"
arcpy.env.overwriteOutput = 1

# inputs (hardcoded)
fire_stations = "C:/Temp/ncshape.mdb/firestations"
schools = "C:/Temp/ncshape.mdb/schools_wake"

# create distance tables for search radius values of 1-5 miles.
radius = 1
while radius <= 5 :
    out_table = "dist%d.dbf" % radius
    search_radius = "%d Miles" % radius
    arcpy.PointDistance_analysis(fire_stations, schools, out_table, search_radius)
    radius += 1