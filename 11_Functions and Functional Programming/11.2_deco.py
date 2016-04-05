 #!/usr/bin/env python

from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrappedFunc

@tsfunc
def foo():
    print 'foo'

foo()
sleep(4)

for i in range(2):
   sleep(1)
   foo()

''' result:
[Mon Apr 04 09:52:48 2016] foo() called
foo
[Mon Apr 04 09:52:53 2016] foo() called
foo
[Mon Apr 04 09:52:54 2016] foo() called
foo
'''