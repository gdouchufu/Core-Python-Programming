#!/usr/bin/env python
import types

def displayNumType(num):
    print num, "is",
    if type(num) is types.IntType: # or : == types.IntType:
        print 'an integer'
    elif type(num) is long:
        print 'a long'
    elif type(num) is float:
        print 'a float'
    elif type(num) is types.ComplexType:
        print 'a complex number'
    else:
        print 'not a number at all!!'

displayNumType(-69)
displayNumType(9999999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')