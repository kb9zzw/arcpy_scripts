#Name: dictionary.py
#Purpose: reports species count and average DBH in RDU Forest
#Modified by: Jon Burroughs (jdburrou), added DBH average to report
#Modified date:  2/27/2012

import string, os.path


filepath = "C:\\temp\\rdu_forest.txt"
data=[]
#Open the text file
myfile=open(filepath,'r')
#Read the text file
### removed this line per kjmario2's catch.  -jdburrou
### myfile.readline() #read the field name line
row = myfile.readline()
count = 0
while row:
    myline = row.split('\t') #Creat a list of the values in this row.  Columns are tab separated.
    #Reads a file with columns: Block Plot  Species DBH MerchHeight
    data.append([float(myline[0]),float(myline[1]),myline[2].rstrip(),float(myline[3].rstrip())]) 
    #rstrip removes white space from the right side
    count = count + 1
    row = myfile.readline()
myfile.close()
mydict={}


#Create an emyty mydict2 here  *********
mydict2 = {}

for row in data:  # for each row
    # create or update a dictionary entry with the current count for that species
    species = row[2]  #Species is the third entry in the file
    DBH = row[3] #DBH is the fourth entry in the file 
    if mydict.has_key(species):  #if a dictionary entry already exists for this species
        #Update dict for this species
        cur_entry = mydict[species]
        cur_entry = int(cur_entry)+1
        mydict[species] = cur_entry
        
        #update mydict2 here  *********
        mydict2[species].append(DBH)

    else:#This is the first dictionary entry for this species
        #Create new dict entry with sums and count for this species
        mydict[species]=1

        #Add a new entry to mydict2 here  *********
        mydict2[species] = [DBH]

mykeys = mydict.keys()
#Print the count for each species
for key in mykeys:
   
    #use mydict2[key] to calculate average for each species here  *********
    average = sum(mydict2[key]) / len(mydict2[key])
   
    count = int(mydict[key])
    print "The number of trees of species", key, "=", count
   
    #print the average for this species here  *********
    print "The average DBH of species", key, "=", average