import time

def iterator_N(N):
    result = 1
    for n in range(1, N+1):
        result *= n
    return result

def reduce_N(N):
    return reduce(lambda x, y : x * y, range(1, N+1))

def recursive_N(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * recursive_N(N-1)

def timeit(func, *nkwargs, **kwargs):
    begin = time.clock()
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval, time.clock()-begin)
    except Exception, diag:
        result = (False, str(diag))
    return result

if __name__ == '__main__':
    funcs = (iterator_N, reduce_N, recursive_N)
    N = 4
    for func in funcs:
        retval = timeit(func, N)
        if retval[0]:
            print '%s(%s) =' % \
                  (func.__name__, `N`), retval[1]
            print 'cost time(s): %s' % `retval[2]`
        else:
            print '%s(%s) = FAILED:' % \
                  (func.__name__, `N`), retval[1]