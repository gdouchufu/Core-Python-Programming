#!/usr/bin/env python
j, k = 1, 2

def proc1():
   j, k = 3, 4
   print "j == %d and k == %d" % (j, k)
   k = 5

def proc2():
    j = 6
    proc1()
    print "j == %d and k == %d" % (j, k)

k = 7
proc1()
print "j == %d and k == %d" % (j, k)

j = 8
proc2()
print "j == %d and k == %d" % (j, k)

'''
j == 3 and k == 4
j == 1 and k == 7
j == 3 and k == 4
j == 6 and k == 7
j == 8 and k == 7
'''