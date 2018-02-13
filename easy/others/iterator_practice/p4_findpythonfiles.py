"""
Problem 4: Write a function to compute the number of python files (.py extension) in a specified directory recursively.

"""
import os
import re
from os.path import join, isfile
def findpythonfiles(dir):
    allitems = (i for i in os.listdir(dir))
    for item in allitems:
        item = join(dir, item)
        if isfile(item):
            if re.search('.*\.py$', item):
                printfilenames(item)
        else:
            findpythonfiles(item)

def printfilenames(f):
    print "<PythonFile> {0}".format(f)
        

findpythonfiles("../..")
