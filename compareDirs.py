#Name:  compareDirs.py
#Purpose:  Compare timestamps of files in one directory vs another
#Usage:  compareDirs.py <workDir> <backupDir>
#Example:  compareDirs.py C:/compareDirs/working C:/compareDirs/backup
#Author:  Jon Burroughs (jdburrou)
#Date: 2/27/2012

import sys, os

def getEpochTime(fullpathFileName):
    # get most recent modification time of the source file in epoch seconds
    return os.path.getmtime(fullpathFileName)
    
if __name__ == '__main__' :

    # get working directory and backup directory from user
    workDir, backupDir = sys.argv[1:3]

    # create dictionary for each list with epoch times
    workDirFiles = {}
    for file in os.listdir(workDir) :
        workDirFiles.update({file: getEpochTime("%s/%s" % (workDir, file))})

    backupDirFiles = {}
    for file in os.listdir(backupDir) :
        backupDirFiles.update({file: getEpochTime("%s/%s" % (backupDir, file))})
    
    # print files to be backed up
    for file,time in workDirFiles.items() :
        if file not in backupDirFiles or time > backupDirFiles[file] :
            print file