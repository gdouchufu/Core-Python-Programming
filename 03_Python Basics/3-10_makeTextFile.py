#!/usr/bin/env python
'makeTextFile.py -- create text file'

import os
ls = os.linesep

# get filename
fname = raw_input('Enter filename: ')
print

# get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

# loop until user terminates input
while True:
    entry = raw_input('$ ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
try:
    fobj = open(fname, 'w')
except IOError, e:
    print "*** file open error:", e
else:
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
