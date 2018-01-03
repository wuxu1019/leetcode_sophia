import os
import site
import sys
#site.addsitedir(os.path.dirname(os.path.abspath(__file__)))
site.addsitedir(os.getcwd())
print os.getcwd()
print os.path.dirname(os.path.abspath(__file__))
print sys.path
