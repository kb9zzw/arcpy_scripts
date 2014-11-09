#Name:  distanceTry.py
#Purpose:  converts miles to kilometers or vice-versa
#Usage:  distanceTry.py <numerical_distance> <distance_unit>
#Example:  distanceTry.py 5 miles
#Author:  Jon Burroughs (jdburrou)
#Date: 2/16/2012

import sys

# get distance value from user (assume they'll provide it correctly)
distance = float(sys.argv[1])

try :
    # attempt to get units from the user.
    units = sys.argv[2].lower()
except IndexError :
    # warn user, then set default units to 'miles'
    print "Warning: no distance_unit was provided.  Default unit, miles used."
    units = "miles"

if units == 'miles' :
    # convert mi to km
    print "%.1f miles is equivalent to %.1f kilometers." % (distance, distance * 1.609344)
elif units == 'kilometers' :
    # conver km to mi
    print "%.1f kilometers is equivalent to %.2f miles." % (distance, distance / 1.609344)
else :
    # punt
    print "I don't know how to convert from '%s', distance_unit should be 'miles' or 'kilometers'." % units