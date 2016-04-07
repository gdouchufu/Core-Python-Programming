import time

def timeit(func, *nkwargs, **kwargs):
    begin = time.clock()
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval, time.clock()-begin)
    except Exception, diag:
        result = (False, str(diag))
    return result

def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '-' * 20
        for eachVal in vals:
            retval = timeit(eachFunc, eachVal)
            if retval[0]:
                print '%s(%s) =' % \
                      (eachFunc.__name__, `eachVal`), retval[1]
                print 'cost time(s): %s' % `retval[2]`
            else:
                print '%s(%s) = FAILED:' % \
                      (eachFunc.__name__, `eachVal`), retval[1]

if __name__ == '__main__':
    test()
