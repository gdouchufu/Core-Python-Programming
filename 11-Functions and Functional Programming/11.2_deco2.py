from time import ctime, sleep

def tsfunc(func):
    print '[%s] %s() call start...' % (ctime(), func.__name__)
    func()
    print '[%s] %s() call end ...' % (ctime(), func.__name__)

def foo():
    print 'foo'

foo()
sleep(1)

for i in range(2):
   sleep(1)
   tsfunc(foo)

''' result:
foo
[Mon Apr 04 10:05:44 2016] foo() call start...
foo
[Mon Apr 04 10:05:44 2016] foo() call end ...
[Mon Apr 04 10:05:45 2016] foo() call start...
foo
[Mon Apr 04 10:05:45 2016] foo() call end ...
'''