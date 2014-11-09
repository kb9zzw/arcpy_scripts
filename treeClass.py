#Name:  treeClass.py
#Purpose:  Reports information about various trees
#Author:  Jon Burroughs (jdburrou)
#Date:  3/15/2012

### Create a class called tree
class tree :
    
    ### Define an __init__ method.  It should assign 4 properties: block, plot, species, and dbh
    '''Initialize tree object properties'''
    def __init__(self, block, plot, species, dbh) :
        self.block = block
        self.plot = plot
        self.species = species
        self.dbh = dbh
    
    ### Define a calculateDIB method which returns diameter inside bark (DIB)
    '''calculate DIB, assuming DIB is diameter breast height times 0.917'''
    def calculateDIB(self) :
        dib = self.dbh * 0.917
        return dib

    ### Define a calculateHeight method which returns the tree height
    '''calculate height, assuming that height = .025*self.dbh + 86.6 for loblolly pines (LP)'''
    '''and height = (.15*self.dbh) + 98.8 for all other species.'''
    def calculateHeight(self) :
        if self.species == 'LP' :
            height = 0.025 * self.dbh + 86.6
        else :
            height = 0.15 * self.dbh + 98.8
            
        return height            

    def report(self, num):
        print "\nReport Tree",num
        print "-------------"
        print "Block: ", self.block
        print "Plot: ", self.plot
        print "Species: ", self.species
        print "DBH: ", self.dbh
        print "DIB: ", self.calculateDIB()
        ### Print the Height as calculated by the calculateHeight method.
        print "Height: ", self.calculateHeight()
        print "\n"


if __name__ == "__main__":        
    t1 = tree(5,91,"SG",14) # Create a tree object t1 from record 1 of rdu_forest.txt
    print "Tree 1 Species:", t1.species  # Print t1's species
    dib = t1.calculateDIB()  # Calculate t1's DIB
    print "Tree 1 DIB:", dib  # Print t1's DIB
    t1.report(1) # report t1 information

    t2 = tree(5,91,"LP",23) # Create a tree object t2 from record 2 of rdu_forest.txt
    
    ### Print t2's DBH
    print "Tree 2 DBH:", t2.dbh
    
    ### Calculate t2's height
    t2_height = t2.calculateHeight()
    
    ### Print t2's height
    print "Tree 2 Height:", t2_height 

    ### Create a tree object t3 from record 3 of rdu_forest.txt
    t3 = tree(5,91,"LP",17)
    
    ### Print t3's block
    print "Tree 3 block:", t3.block
    
    ### Print t3's plot
    print "Tree 3 plot:", t3.plot

    ### Create a tree object t4 from record 4 of rdu_forest.txt
    t4 = tree(5,91,"LP",18)
    
    ### report t4 information
    t4.report(4)

