# Name: lineSegmentClass.py
# Purpose:  Methods for calculating various parameters of line segments
# Author:  Jon Burroughs (jdburrou)
# Date:  3/15/2012

import math

class lineSegment:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculateLength(self):
        '''Calculate the length of this line segment'''
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)

    def calculateSlope(self):
        '''Calculate the slope of this line segment.'''
        run = self.x2 - self.x1
        if run == 0:
            return "undefined"
        else:
            return (self.y2 - self.y1)/float(run)

    def translateY(self, yShift):
        '''Translate the line vertically by yShift
        (Shifts the line segment up or down.)'''
        self.y1 = self.y1 + yShift
        self.y2 = self.y2 + yShift

if __name__ == '__main__' :
    # instantiate lineSegment
    ls = lineSegment(1,2,4,3)

    # print output
    print "(%d,%d)" % (ls.x1, ls.y1)
    print "(%d,%d)" % (ls.x2, ls.y2)
    print "Slope:", ls.calculateSlope()
    print "Length:", ls.calculateLength()
    ls.translateY(-3)
    print "(%d,%d)" % (ls.x1, ls.y1)
    print "(%d,%d)" % (ls.x2, ls.y2)

