#!/usr/bin/env python
import string

def des_sort_numstr_by_decimal(numstr):
    numlist = numstr.split(',')
    for i in range(0, len(numlist)):
        numlist[i] = int(numlist[i])
    
    numlist.sort()
    numlist.reverse()
    return numlist
def des_sort_numstr_by_dictionary(numstr):
    numlist = numstr.split(',')
    numlist.sort()
    numlist.reverse()
    return numlist

if __name__ == '__main__':
    numstr = raw_input('input some number: ')
    print "before sort: " + numstr
    print "sort by decimal: " + str(des_sort_numstr_by_decimal(numstr))
    print "sort by dictionary: " + str(des_sort_numstr_by_dictionary(numstr))