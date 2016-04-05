#!/usr/bin/env python

import os
ls = os.linesep

def readFile():
    # get filename
    fname = raw_input('Enter filename: ')
    print

    # attempt to open file for reading
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "*** file open error:", e
    else:
        # display contents to the screen
        for eachLine in fobj:
            print eachLine,
        fobj.close()

def writeFile():
    # get filename
    while True:
        fname = raw_input('Enter filename: ')
        print

        if os.path.exists(fname):
           print "ERROR: '%s' already exists" % fname
        else:
           break

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
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()

while True:
    choose = raw_input('choose action: r | w :')
    if (choose == 'r'):
        readFile()
        break
    elif (choose == 'w'):
        writeFile()
        break