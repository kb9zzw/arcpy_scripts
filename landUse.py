#Name:  landUse.py
#Purpose:  Fun with dictionaries
#Usage:  landUse.py
#Author:  Jon Burroughs (jdburrou)
#Date:  2/27/2012

landUse = {'res': 1, 'com': 2, 'int': 3, 'other' :[4,5,6,7]}

#1
print landUse['com']
#2
print landUse.has_key('res')
#3
print landUse['int']
#4
landUse['agr'] = 0
print landUse
#5
landUse['res'] = 10
print landUse
#6
print landUse.keys()
#7
for value in landUse.values() :
    print value
#8
print landUse.items()
#9
del landUse['int']
print landUse
#10
print 'int' in landUse


    