#!/usr/bin/env python
import os
'readTextFile.py -- read and display text file'

# get filename
fname = raw_input('Enter filename: ')
print

# attempt to open file for reading
if not os.path.exists(fname):
	print "ERROR: '%s' not exists" % fname
else:
    fobj = open(fname, 'r')
    # display contents to the screen
    for eachLine in fobj:
        print eachLine.strip()
    fobj.close()

    
