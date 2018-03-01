"""
Problem 3: Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

"""
import os
from os.path import isfile, join

def readfolder(mydir):
    allitems = (i for i in os.listdir(mydir))
    for item in allitems:
        item = join(mydir, item)
        if isfile(item):
            print "<File> {0}".format(item)
        else:
            print "<Folder> {0}".format(item)
            readfolder(item)

readfolder('../')

    
